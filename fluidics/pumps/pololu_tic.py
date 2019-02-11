#!/usr/bin/python
# ----------------------------------------------------------------------------------------
# The basic I/O class for a Pololu TIC stepper driver
# ----------------------------------------------------------------------------------------
# Nasa Sinnott-Armstrong
# 02/10/19
# nasa@stanford.edu
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------------------------
import serial
import time
import tic
import constants

acknowledge = '\x06'
start = '\x0A'
stop = '\x0D'

# ----------------------------------------------------------------------------------------
# TIC Class Definition
# ----------------------------------------------------------------------------------------
class APump():
    def __init__(self,
                 parameters = False):

        self.tic = tic.TicDevice()

        pumpsn = parameters.get("pump_ID", None)
        if pumpsn is not None and pumpsn != "":
            self.tic.open(vendor=0x1ffb, product_id=0x00b3, serial=pumpsn)
        else:
            self.tic.open(vendor=0x1ffb, product_id=0x00b3)

        self.tic.reset()

        self.tic.set_max_speed(2000000)
        self.tic.set_max_accel(50000)
        self.tic.set_max_decel(800000)
        self.tic.exit_safe_start()
        self.tic.set_decay_mode(constants.TIC_DECAY_MODE_T825_MIXED)
        self.tic.set_starting_speed(10000)
        self.tic.halt_and_set_position(0)

        self.tic.deenergize()

        # Define attributes
        self.verbose = parameters.get("verbose", True)
        self.simulate = parameters.get("simulate_pump", True)
        self.serial_verbose = parameters.get("serial_verbose", False)
        self.flip_flow_direction = parameters.get("flip_flow_direction", False)

        # Define initial pump status
        self.flow_status = "Stopped"
        self.speed = 0.0
        self.direction = "Forward"
        self.identification = "Pololu Tic"

    def getIdentification(self):
        return self.sendImmediate(self.pump_ID, "%")

    def readDisplay(self):
        return self.sendImmediate(self.pump_ID, "R")

    def getStatus(self):
        v = self.tic.get_variables()

        status = "Stopped" if v["current_velocity"] == 0 else "Flowing"
        speed = v["current_velocity"]/(40000.)
        direction = "Forward" if self.direction > 0 else "Reverse"
        return (status, speed, direction, "K", "Disabled", "No Error")

    def close(self):
        self.tic.close()

    def setFlowDirection(self, forward):
        if self.flip_flow_direction:
            if forward:
                self.direction = -1
            else:
                self.direction = 1
        else:
            if forward:
                self.direction = 1
            else:
                self.direction = -1
        self.setSpeed(abs(self.speed) * self.direction)
    
    def setSpeed(self, rotation_speed):
        self.speed = rotation_speed
        if rotation_speed >= 0 and rotation_speed < 2**24:
            self.tic.set_target_velocity(self.direction * int(rotation_speed * 40000))

    def startFlow(self, speed, direction = "Forward"):
        self.tic.exit_safe_start()
        self.tic.energize()
        self.setFlowDirection(direction == "Forward")
        self.setSpeed(speed)

    def stopFlow(self):
        self.setSpeed(0.0)
        self.tic.enter_safe_start()
        self.tic.deenergize()
        self.tic.halt_and_set_position(0)
        return True


    def disconnect(self):
        return self.stopFlow()

    def selectUnit(self, unitNumber):
        return True
