# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steve.ui'
#
# Created: Wed Jul  8 12:21:08 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1148, 831)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mosaicTab = QtGui.QWidget()
        self.mosaicTab.setObjectName(_fromUtf8("mosaicTab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.mosaicTab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mosaicFrame = QtGui.QFrame(self.mosaicTab)
        self.mosaicFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mosaicFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mosaicFrame.setObjectName(_fromUtf8("mosaicFrame"))
        self.horizontalLayout_2.addWidget(self.mosaicFrame)
        self.widget = QtGui.QWidget(self.mosaicTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.positionsGroupBox = QtGui.QGroupBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.positionsGroupBox.sizePolicy().hasHeightForWidth())
        self.positionsGroupBox.setSizePolicy(sizePolicy)
        self.positionsGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.positionsGroupBox.setMaximumSize(QtCore.QSize(10000, 10000))
        self.positionsGroupBox.setObjectName(_fromUtf8("positionsGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.positionsGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.positionsFrame = QtGui.QFrame(self.positionsGroupBox)
        self.positionsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.positionsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.positionsFrame.setObjectName(_fromUtf8("positionsFrame"))
        self.verticalLayout_4.addWidget(self.positionsFrame)
        self.verticalLayout_2.addWidget(self.positionsGroupBox)
        self.tilesGroupBox = QtGui.QGroupBox(self.widget)
        self.tilesGroupBox.setMinimumSize(QtCore.QSize(300, 150))
        self.tilesGroupBox.setMaximumSize(QtCore.QSize(300, 300))
        self.tilesGroupBox.setObjectName(_fromUtf8("tilesGroupBox"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tilesGroupBox)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.startingPositionLabel = QtGui.QLabel(self.tilesGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.startingPositionLabel.setFont(font)
        self.startingPositionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.startingPositionLabel.setObjectName(_fromUtf8("startingPositionLabel"))
        self.verticalLayout_3.addWidget(self.startingPositionLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.xPosLabel = QtGui.QLabel(self.tilesGroupBox)
        self.xPosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xPosLabel.setObjectName(_fromUtf8("xPosLabel"))
        self.horizontalLayout_4.addWidget(self.xPosLabel)
        self.xStartPosSpinBox = QtGui.QDoubleSpinBox(self.tilesGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xStartPosSpinBox.sizePolicy().hasHeightForWidth())
        self.xStartPosSpinBox.setSizePolicy(sizePolicy)
        self.xStartPosSpinBox.setMinimum(-50000.0)
        self.xStartPosSpinBox.setMaximum(50000.0)
        self.xStartPosSpinBox.setObjectName(_fromUtf8("xStartPosSpinBox"))
        self.horizontalLayout_4.addWidget(self.xStartPosSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.yPosLabel = QtGui.QLabel(self.tilesGroupBox)
        self.yPosLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yPosLabel.setObjectName(_fromUtf8("yPosLabel"))
        self.horizontalLayout_6.addWidget(self.yPosLabel)
        self.yStartPosSpinBox = QtGui.QDoubleSpinBox(self.tilesGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yStartPosSpinBox.sizePolicy().hasHeightForWidth())
        self.yStartPosSpinBox.setSizePolicy(sizePolicy)
        self.yStartPosSpinBox.setMinimum(-50000.0)
        self.yStartPosSpinBox.setMaximum(500000.0)
        self.yStartPosSpinBox.setObjectName(_fromUtf8("yStartPosSpinBox"))
        self.horizontalLayout_6.addWidget(self.yStartPosSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridDimLabel = QtGui.QLabel(self.tilesGroupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.gridDimLabel.setFont(font)
        self.gridDimLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridDimLabel.setObjectName(_fromUtf8("gridDimLabel"))
        self.verticalLayout_7.addWidget(self.gridDimLabel)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.numXLabel = QtGui.QLabel(self.tilesGroupBox)
        self.numXLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numXLabel.setObjectName(_fromUtf8("numXLabel"))
        self.horizontalLayout_5.addWidget(self.numXLabel)
        self.xSpinBox = QtGui.QSpinBox(self.tilesGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xSpinBox.sizePolicy().hasHeightForWidth())
        self.xSpinBox.setSizePolicy(sizePolicy)
        self.xSpinBox.setMinimum(1)
        self.xSpinBox.setProperty("value", 5)
        self.xSpinBox.setObjectName(_fromUtf8("xSpinBox"))
        self.horizontalLayout_5.addWidget(self.xSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.numYLabel = QtGui.QLabel(self.tilesGroupBox)
        self.numYLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numYLabel.setObjectName(_fromUtf8("numYLabel"))
        self.horizontalLayout_7.addWidget(self.numYLabel)
        self.ySpinBox = QtGui.QSpinBox(self.tilesGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ySpinBox.sizePolicy().hasHeightForWidth())
        self.ySpinBox.setSizePolicy(sizePolicy)
        self.ySpinBox.setMinimum(1)
        self.ySpinBox.setProperty("value", 3)
        self.ySpinBox.setObjectName(_fromUtf8("ySpinBox"))
        self.horizontalLayout_7.addWidget(self.ySpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.getStagePosButton = QtGui.QPushButton(self.tilesGroupBox)
        self.getStagePosButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.getStagePosButton.setObjectName(_fromUtf8("getStagePosButton"))
        self.horizontalLayout_10.addWidget(self.getStagePosButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.imageGridButton = QtGui.QPushButton(self.tilesGroupBox)
        self.imageGridButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.imageGridButton.setObjectName(_fromUtf8("imageGridButton"))
        self.horizontalLayout_10.addWidget(self.imageGridButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addWidget(self.tilesGroupBox)
        self.objectivesGroupBox = ObjectivesGroupBox(self.widget)
        self.objectivesGroupBox.setMinimumSize(QtCore.QSize(250, 50))
        self.objectivesGroupBox.setMaximumSize(QtCore.QSize(300, 300))
        self.objectivesGroupBox.setObjectName(_fromUtf8("objectivesGroupBox"))
        self.verticalLayout_2.addWidget(self.objectivesGroupBox)
        self.miscGroupBox = QtGui.QGroupBox(self.widget)
        self.miscGroupBox.setMinimumSize(QtCore.QSize(0, 20))
        self.miscGroupBox.setObjectName(_fromUtf8("miscGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.miscGroupBox)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.trackStageCheckBox = QtGui.QCheckBox(self.miscGroupBox)
        self.trackStageCheckBox.setObjectName(_fromUtf8("trackStageCheckBox"))
        self.horizontalLayout.addWidget(self.trackStageCheckBox)
        self.scaleLabel = QtGui.QLabel(self.miscGroupBox)
        self.scaleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scaleLabel.setObjectName(_fromUtf8("scaleLabel"))
        self.horizontalLayout.addWidget(self.scaleLabel)
        self.scaleLineEdit = QtGui.QLineEdit(self.miscGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleLineEdit.sizePolicy().hasHeightForWidth())
        self.scaleLineEdit.setSizePolicy(sizePolicy)
        self.scaleLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scaleLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scaleLineEdit.setObjectName(_fromUtf8("scaleLineEdit"))
        self.horizontalLayout.addWidget(self.scaleLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.cursorPosition = QtGui.QLabel(self.miscGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cursorPosition.sizePolicy().hasHeightForWidth())
        self.cursorPosition.setSizePolicy(sizePolicy)
        self.cursorPosition.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cursorPosition.setObjectName(_fromUtf8("cursorPosition"))
        self.horizontalLayout_9.addWidget(self.cursorPosition)
        self.mosaicLabel = QtGui.QLabel(self.miscGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mosaicLabel.sizePolicy().hasHeightForWidth())
        self.mosaicLabel.setSizePolicy(sizePolicy)
        self.mosaicLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mosaicLabel.setObjectName(_fromUtf8("mosaicLabel"))
        self.horizontalLayout_9.addWidget(self.mosaicLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addWidget(self.miscGroupBox)
        self.horizontalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.mosaicTab, _fromUtf8(""))
        self.sectionsTab = QtGui.QWidget()
        self.sectionsTab.setObjectName(_fromUtf8("sectionsTab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.sectionsTab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.sectionsDisplayFrame = QtGui.QFrame(self.sectionsTab)
        self.sectionsDisplayFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sectionsDisplayFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sectionsDisplayFrame.setObjectName(_fromUtf8("sectionsDisplayFrame"))
        self.horizontalLayout_3.addWidget(self.sectionsDisplayFrame)
        self.sectionsWidget = QtGui.QWidget(self.sectionsTab)
        self.sectionsWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.sectionsWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sectionsWidget.setObjectName(_fromUtf8("sectionsWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.sectionsWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.sectionsGroupBox = QtGui.QGroupBox(self.sectionsWidget)
        self.sectionsGroupBox.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.sectionsGroupBox.setObjectName(_fromUtf8("sectionsGroupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.sectionsGroupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.sectionsScrollArea = QtGui.QScrollArea(self.sectionsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionsScrollArea.sizePolicy().hasHeightForWidth())
        self.sectionsScrollArea.setSizePolicy(sizePolicy)
        self.sectionsScrollArea.setWidgetResizable(True)
        self.sectionsScrollArea.setObjectName(_fromUtf8("sectionsScrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 254, 533))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.sectionsScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.sectionsScrollArea)
        self.verticalLayout_5.addWidget(self.sectionsGroupBox)
        self.sectionViewSettingsGroupBox = QtGui.QGroupBox(self.sectionsWidget)
        self.sectionViewSettingsGroupBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.sectionViewSettingsGroupBox.setObjectName(_fromUtf8("sectionViewSettingsGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.sectionViewSettingsGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.thresholdLabel = QtGui.QLabel(self.sectionViewSettingsGroupBox)
        self.thresholdLabel.setObjectName(_fromUtf8("thresholdLabel"))
        self.gridLayout.addWidget(self.thresholdLabel, 1, 0, 1, 1)
        self.foregroundOpacitySlider = QtGui.QSlider(self.sectionViewSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foregroundOpacitySlider.sizePolicy().hasHeightForWidth())
        self.foregroundOpacitySlider.setSizePolicy(sizePolicy)
        self.foregroundOpacitySlider.setMaximum(100)
        self.foregroundOpacitySlider.setProperty("value", 50)
        self.foregroundOpacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.foregroundOpacitySlider.setObjectName(_fromUtf8("foregroundOpacitySlider"))
        self.gridLayout.addWidget(self.foregroundOpacitySlider, 4, 1, 1, 1)
        self.moveAllSectionsCheckBox = QtGui.QCheckBox(self.sectionViewSettingsGroupBox)
        self.moveAllSectionsCheckBox.setObjectName(_fromUtf8("moveAllSectionsCheckBox"))
        self.gridLayout.addWidget(self.moveAllSectionsCheckBox, 0, 0, 1, 1)
        self.foregroundOpacityLabel = QtGui.QLabel(self.sectionViewSettingsGroupBox)
        self.foregroundOpacityLabel.setObjectName(_fromUtf8("foregroundOpacityLabel"))
        self.gridLayout.addWidget(self.foregroundOpacityLabel, 4, 0, 1, 1)
        self.showFeaturesCheckBox = QtGui.QCheckBox(self.sectionViewSettingsGroupBox)
        self.showFeaturesCheckBox.setObjectName(_fromUtf8("showFeaturesCheckBox"))
        self.gridLayout.addWidget(self.showFeaturesCheckBox, 0, 1, 1, 1)
        self.backgroundLabel = QtGui.QLabel(self.sectionViewSettingsGroupBox)
        self.backgroundLabel.setObjectName(_fromUtf8("backgroundLabel"))
        self.gridLayout.addWidget(self.backgroundLabel, 2, 0, 1, 1)
        self.backgroundComboBox = QtGui.QComboBox(self.sectionViewSettingsGroupBox)
        self.backgroundComboBox.setObjectName(_fromUtf8("backgroundComboBox"))
        self.backgroundComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.backgroundComboBox, 2, 1, 1, 1)
        self.thresholdSlider = QtGui.QSlider(self.sectionViewSettingsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSlider.sizePolicy().hasHeightForWidth())
        self.thresholdSlider.setSizePolicy(sizePolicy)
        self.thresholdSlider.setMaximum(100)
        self.thresholdSlider.setProperty("value", 50)
        self.thresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.thresholdSlider.setObjectName(_fromUtf8("thresholdSlider"))
        self.gridLayout.addWidget(self.thresholdSlider, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.sectionViewSettingsGroupBox)
        self.horizontalLayout_3.addWidget(self.sectionsWidget)
        self.tabWidget.addTab(self.sectionsTab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionSave_Positions = QtGui.QAction(MainWindow)
        self.actionSave_Positions.setObjectName(_fromUtf8("actionSave_Positions"))
        self.actionSave_Mosaic = QtGui.QAction(MainWindow)
        self.actionSave_Mosaic.setObjectName(_fromUtf8("actionSave_Mosaic"))
        self.actionSet_Working_Directory = QtGui.QAction(MainWindow)
        self.actionSet_Working_Directory.setObjectName(_fromUtf8("actionSet_Working_Directory"))
        self.actionLoad_Mosaic = QtGui.QAction(MainWindow)
        self.actionLoad_Mosaic.setObjectName(_fromUtf8("actionLoad_Mosaic"))
        self.actionDelete_Images = QtGui.QAction(MainWindow)
        self.actionDelete_Images.setObjectName(_fromUtf8("actionDelete_Images"))
        self.actionLoad_Positions = QtGui.QAction(MainWindow)
        self.actionLoad_Positions.setObjectName(_fromUtf8("actionLoad_Positions"))
        self.actionSave_Snapshot = QtGui.QAction(MainWindow)
        self.actionSave_Snapshot.setObjectName(_fromUtf8("actionSave_Snapshot"))
        self.actionLoad_Movie = QtGui.QAction(MainWindow)
        self.actionLoad_Movie.setObjectName(_fromUtf8("actionLoad_Movie"))
        self.actionLoad_Dax_By_Pattern = QtGui.QAction(MainWindow)
        self.actionLoad_Dax_By_Pattern.setObjectName(_fromUtf8("actionLoad_Dax_By_Pattern"))
        self.actionAdjust_Contrast = QtGui.QAction(MainWindow)
        self.actionAdjust_Contrast.setObjectName(_fromUtf8("actionAdjust_Contrast"))
        self.menuFile.addAction(self.actionSet_Working_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDelete_Images)
        self.menuFile.addAction(self.actionLoad_Movie)
        self.menuFile.addAction(self.actionLoad_Mosaic)
        self.menuFile.addAction(self.actionLoad_Positions)
        self.menuFile.addAction(self.actionSave_Mosaic)
        self.menuFile.addAction(self.actionSave_Positions)
        self.menuFile.addAction(self.actionSave_Snapshot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionAdjust_Contrast)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.xStartPosSpinBox, self.yStartPosSpinBox)
        MainWindow.setTabOrder(self.yStartPosSpinBox, self.xSpinBox)
        MainWindow.setTabOrder(self.xSpinBox, self.ySpinBox)
        MainWindow.setTabOrder(self.ySpinBox, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.foregroundOpacitySlider)
        MainWindow.setTabOrder(self.foregroundOpacitySlider, self.backgroundComboBox)
        MainWindow.setTabOrder(self.backgroundComboBox, self.thresholdSlider)
        MainWindow.setTabOrder(self.thresholdSlider, self.showFeaturesCheckBox)
        MainWindow.setTabOrder(self.showFeaturesCheckBox, self.moveAllSectionsCheckBox)
        MainWindow.setTabOrder(self.moveAllSectionsCheckBox, self.sectionsScrollArea)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Steve", None))
        self.positionsGroupBox.setTitle(_translate("MainWindow", "Positions", None))
        self.tilesGroupBox.setTitle(_translate("MainWindow", "Tile Settings", None))
        self.startingPositionLabel.setText(_translate("MainWindow", "Center", None))
        self.xPosLabel.setText(_translate("MainWindow", "X:", None))
        self.yPosLabel.setText(_translate("MainWindow", "Y:", None))
        self.gridDimLabel.setText(_translate("MainWindow", "Grid Size", None))
        self.numXLabel.setText(_translate("MainWindow", "# X:", None))
        self.numYLabel.setText(_translate("MainWindow", "# Y:", None))
        self.getStagePosButton.setText(_translate("MainWindow", "Get Stage Position", None))
        self.imageGridButton.setText(_translate("MainWindow", "Acquire", None))
        self.objectivesGroupBox.setTitle(_translate("MainWindow", "Objective Settings", None))
        self.miscGroupBox.setTitle(_translate("MainWindow", "Misc", None))
        self.trackStageCheckBox.setText(_translate("MainWindow", "Track Stage", None))
        self.scaleLabel.setText(_translate("MainWindow", "Scale:", None))
        self.scaleLineEdit.setText(_translate("MainWindow", "1.0", None))
        self.cursorPosition.setText(_translate("MainWindow", "Cursor:", None))
        self.mosaicLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mosaicTab), _translate("MainWindow", "Mosaic", None))
        self.sectionsGroupBox.setTitle(_translate("MainWindow", "Sections", None))
        self.sectionViewSettingsGroupBox.setTitle(_translate("MainWindow", "Section View Settings", None))
        self.thresholdLabel.setText(_translate("MainWindow", "Threshold", None))
        self.moveAllSectionsCheckBox.setText(_translate("MainWindow", "Move All Sections", None))
        self.foregroundOpacityLabel.setText(_translate("MainWindow", "Section Opacity", None))
        self.showFeaturesCheckBox.setText(_translate("MainWindow", "Show Features", None))
        self.backgroundLabel.setText(_translate("MainWindow", "Background Type", None))
        self.backgroundComboBox.setItemText(0, _translate("MainWindow", "Mean", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sectionsTab), _translate("MainWindow", "Sections", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit (Ctrl+Q)", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.actionSave_Positions.setText(_translate("MainWindow", "Save Positions", None))
        self.actionSave_Positions.setShortcut(_translate("MainWindow", "Ctrl+T", None))
        self.actionSave_Mosaic.setText(_translate("MainWindow", "Save Mosaic", None))
        self.actionSave_Mosaic.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSet_Working_Directory.setText(_translate("MainWindow", "Set Working Directory", None))
        self.actionLoad_Mosaic.setText(_translate("MainWindow", "Load Mosaic", None))
        self.actionLoad_Mosaic.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.actionDelete_Images.setText(_translate("MainWindow", "Delete Images", None))
        self.actionDelete_Images.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.actionLoad_Positions.setText(_translate("MainWindow", "Load Positions", None))
        self.actionLoad_Positions.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionSave_Snapshot.setText(_translate("MainWindow", "Save Snapshot", None))
        self.actionSave_Snapshot.setShortcut(_translate("MainWindow", "Ctrl+I", None))
        self.actionLoad_Movie.setText(_translate("MainWindow", "Load Movie", None))
        self.actionLoad_Movie.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionLoad_Dax_By_Pattern.setText(_translate("MainWindow", "Load Dax By Pattern", None))
        self.actionAdjust_Contrast.setText(_translate("MainWindow", "Adjust Contrast (Ctrl+C)", None))
        self.actionAdjust_Contrast.setShortcut(_translate("MainWindow", "Ctrl+C", None))

from objectives import ObjectivesGroupBox
