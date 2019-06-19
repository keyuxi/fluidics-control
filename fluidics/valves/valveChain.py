#!/usr/bin/python
# ----------------------------------------------------------------------------------------
# A wrapper class for the Hamilton MVP valve chain and the Widgets that display
# their status.  All interactions with the valve chain should go through this
# class.
# ----------------------------------------------------------------------------------------
# Jeff Moffitt
# 12/28/13
# jeffmoffitt@gmail.com
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------------------------
import sys
from PyQt4 import QtCore, QtGui
from valves.qtValveControl import QtValveControl
from valves.hamilton import HamiltonMVP

from valves.autopicker import MockAutopicker
from valves.autopicker_cnc import CNC
from valves.autopicker_xyz import XYZ

# ----------------------------------------------------------------------------------------
# ValveChain Class Definition
# ----------------------------------------------------------------------------------------
class ValveChain(QtGui.QWidget):
    def __init__(self,
                 parent = None,
                 com_port = 2,
                 num_simulated_valves = 0,
                 usb_cnc = False,
                 verbose = False
                 ):

        # Initialize parent class
        QtGui.QWidget.__init__(self, parent)

        # Define local attributes
        self.com_port = com_port
        self.verbose = verbose
        self.poll_time = 2000

        # Create instance of Hamilton class
        if self.com_port < 0 or num_simulated_valves > 0:
            print('simulating valves')
            self.valve_chain = HamiltonMVP(com_port = -1,
                                           num_simulated_valves = num_simulated_valves,
                                           verbose = self.verbose)
        else:
            self.valve_chain = HamiltonMVP(com_port = self.com_port,
                                           verbose = self.verbose)

        if usb_cnc:
            if isinstance(usb_cnc, tuple) or isinstance(usb_cnc, list):
                self.cnc = CNC(usb_cnc[0], usb_cnc[1])
            elif usb_cnc == "simulated":
                self.cnc = MockAutopicker()
            elif usb_cnc == "XYZ":
                self.cnc = XYZ()
            else:
                self.cnc = CNC()
        else:
            self.cnc = None

        # Create QtValveControl widgets for each valve in the chain
        self.num_valves = self.valve_chain.howManyValves()
        self.valve_names = []
        self.valve_widgets = []
        
        # Create GUI
        self.createGUI() # Widgets created here

        # Define timer for periodic polling of valve status
        self.valve_poll_timer = QtCore.QTimer()        
        self.valve_poll_timer.setInterval(self.poll_time)
        self.valve_poll_timer.timeout.connect(self.pollValveStatus)
        self.valve_poll_timer.start()

    # ------------------------------------------------------------------------------------
    # Change specified valve position
    # ------------------------------------------------------------------------------------
    def changeValvePosition(self, valve_ID, port_ID = None):
        print("Valve", valve_ID, "and port", port_ID)

        if valve_ID >= 0 and valve_ID < self.num_valves:
            if port_ID == None:
                port_ID = self.valve_widgets[valve_ID].getPortIndex()
            rotation_direction = self.valve_widgets[valve_ID].getDesiredRotationIndex()
        else:
            if port_ID == None:
                port_ID = self.valve_widgets[-1].getPortIndex()
            rotation_direction = self.valve_widgets[-1].getDesiredRotationIndex()

        if self.verbose:
            text_string = "Changing Valve " + str(valve_ID)
            text_string += " Port " + str(port_ID)
            text_string += " Direction " + str(rotation_direction)
            print(text_string )
        
        if valve_ID >= 0 and valve_ID < self.num_valves:
            if port_ID == None:
                port_ID = self.valve_widgets[valve_ID].getPortIndex()
            rotation_direction = self.valve_widgets[valve_ID].getDesiredRotationIndex()

            self.valve_chain.changePort(valve_ID = valve_ID,
                                    port_ID = port_ID,
                                    direction = rotation_direction)
        else:
            self.cnc.move(port_ID, direction = rotation_direction)

        # Update valve display
        self.pollValveStatus()

    # ------------------------------------------------------------------------------------
    # Close class
    # ------------------------------------------------------------------------------------
    def close(self):
        if self.verbose: print("Closing valve chain")
        self.valve_chain.close()
        if self.cnc is not None:
            print("Closing USB CNC")
            self.cnc.close()

    # ------------------------------------------------------------------------------------
    # Create the Qt widgets for display
    # ------------------------------------------------------------------------------------  
    def createGUI(self):
        # Define display widget
        self.valveChainGroupBox = QtGui.QGroupBox()
        self.valveChainGroupBox.setTitle("Valve Controls")
        self.valveChainGroupBoxLayout = QtGui.QVBoxLayout(self.valveChainGroupBox)

        for valve_ID in range(self.num_valves):
            valve_widget = QtValveControl(self,
                                         ID = valve_ID)
            self.valve_names.append(str(valve_ID + 1)) # Save valve name
            valve_widget.setValveName("Valve " + str(valve_ID+1)) # Valve names are +1 valve IDs
            valve_widget.setValveConfiguration(self.valve_chain.howIsValveConfigured(valve_ID))
            valve_widget.setPortNames(self.valve_chain.getDefaultPortNames(valve_ID))
            valve_widget.setRotationDirections(self.valve_chain.getRotationDirections(valve_ID))
            valve_widget.setStatus(self.valve_chain.getStatus(valve_ID))

            valve_widget.change_port_signal.connect(self.changeValvePosition)

            self.valve_widgets.append(valve_widget)

            self.valveChainGroupBoxLayout.addWidget(valve_widget)

        if self.cnc is not None:
            cnc_widget = QtValveControl(self, ID = -2)
            cnc_widget.setValveName("CNC") # Valve names are +1 valve IDs
            cnc_widget.setValveConfiguration(self.cnc.get_configuration())
            cnc_widget.setPortNames(self.cnc.get_wells())
            cnc_widget.setRotationDirections(self.cnc.get_plates())
            cnc_widget.setStatus(self.cnc.get_status())
            self.valve_names.append("CNC")

            cnc_widget.change_port_signal.connect(self.changeValvePosition)

            self.valve_widgets.append(cnc_widget)

            self.valveChainGroupBoxLayout.addWidget(cnc_widget)

        self.valveChainGroupBoxLayout.addStretch(1)

        # Define main widget
        self.mainWidget = self.valveChainGroupBox

        # Define menu items
        self.valve_reset_action = QtGui.QAction("Valve Chain Reset", self)
        self.valve_reset_action.triggered.connect(self.reinitializeChain)

        self.menu_names = ["Valve"]
        self.menu_items = [[self.valve_reset_action]]

    # ------------------------------------------------------------------------------------
    # Determine number of valves
    # ------------------------------------------------------------------------------------
    def howManyValves(self):
        return self.valve_chain.howManyValves + (self.cnc is not None)

    # ------------------------------------------------------------------------------------
    # Update valve status display with the current status each valve in the chain
    # ------------------------------------------------------------------------------------
    def pollValveStatus(self):
        for valve_ID in range(self.num_valves):
            self.valve_widgets[valve_ID].setStatus(self.valve_chain.getStatus(valve_ID))
        if self.cnc is not None:
            self.valve_widgets[-1].setStatus(self.cnc.get_status())

    # ------------------------------------------------------------------------------------
    # Change port status based on external command
    # ------------------------------------------------------------------------------------          
    def receiveCommand(self, command):
        for valve_ID, port_ID in enumerate(command):
            if port_ID >= 0: # -1 is a flag for 'do not change port'
                self.changeValvePosition(valve_ID, port_ID)

    # ------------------------------------------------------------------------------------
    # Reinitialize the valve chain
    # ------------------------------------------------------------------------------------          
    def reinitializeChain(self):
        self.valve_chain.resetChain()
        #if self.cnc is not None:
        #    self.cnc.reset()

    # ------------------------------------------------------------------------------------
    # Set enabled status for display items
    # ------------------------------------------------------------------------------------          
    def setEnabled(self, is_enabled):
        for valve_ID in range(self.num_valves):
            self.valve_widgets[valve_ID].setEnabled(is_enabled)
        if self.cnc is not None:
            self.valve_widgets[-1].setEnabled(is_enabled)
    
# ----------------------------------------------------------------------------------------
# Stand Alone Test Class
# ----------------------------------------------------------------------------------------
class StandAlone(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(StandAlone, self).__init__(parent)

        # scroll area widget contents - layout
        self.valve_chain = ValveChain(COM_port = 2,
                                      verbose = True,
                                      num_simulated_valves = 2)
        
        # central widget
        self.centralWidget = QtGui.QWidget()
        self.mainLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.mainLayout.addWidget(self.valve_chain.mainWidget)
        
        # set central widget
        self.setCentralWidget(self.centralWidget)

        # set window title
        self.setWindowTitle("Valve Chain Control")

        # set window geometry
        self.setGeometry(50, 50, 500, 100 + 100*self.valve_chain.num_valves)

        # Create file menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        exit_action = QtGui.QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.closeEvent)

        file_menu.addAction(exit_action)

    # ------------------------------------------------------------------------------------
    # Detect close event
    # ------------------------------------------------------------------------------------    
    def closeEvent(self, event):
        self.valve_chain.close()
        self.close()

# ----------------------------------------------------------------------------------------
# Test/Demo of Classs
# ----------------------------------------------------------------------------------------        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = StandAlone()
    window.show()
    app.exec_()                              

#
# The MIT License
#
# Copyright (c) 2013 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

