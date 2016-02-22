# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './source/mainwindow.ui'
#
# Created by: ...third_party.qtpy UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from ...third_party.qtpy import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralWidget)
        self.mdiArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mdiArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mdiArea.setLineWidth(2)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuDocks = QtWidgets.QMenu(self.menuBar)
        self.menuDocks.setObjectName("menuDocks")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(False)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(176, 267))
        self.dockWidget.setFloating(False)
        self.dockWidget.setWindowTitle("Data")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.dockWidgetContents)
        self.toolButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Template-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.dockWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Change Theme-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.dataRemoveButton = QtWidgets.QToolButton(self.dockWidgetContents)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Delete-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dataRemoveButton.setIcon(icon2)
        self.dataRemoveButton.setIconSize(QtCore.QSize(20, 20))
        self.dataRemoveButton.setObjectName("dataRemoveButton")
        self.horizontalLayout_2.addWidget(self.dataRemoveButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setWindowTitle("Statistics")
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.currentLayerLabel = QtWidgets.QLabel(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLayerLabel.sizePolicy().hasHeightForWidth())
        self.currentLayerLabel.setSizePolicy(sizePolicy)
        self.currentLayerLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.currentLayerLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentLayerLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentLayerLabel.setObjectName("currentLayerLabel")
        self.verticalLayout_7.addWidget(self.currentLayerLabel)
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget.setObjectName("tabWidget")
        self.basicTab = QtWidgets.QWidget()
        self.basicTab.setObjectName("basicTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.basicTab)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(1, 1, 1, 1)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.meanLabel = QtWidgets.QLabel(self.basicTab)
        self.meanLabel.setObjectName("meanLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.meanLabel)
        self.meanLineEdit = QtWidgets.QLineEdit(self.basicTab)
        self.meanLineEdit.setReadOnly(True)
        self.meanLineEdit.setObjectName("meanLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.meanLineEdit)
        self.medianLabel = QtWidgets.QLabel(self.basicTab)
        self.medianLabel.setObjectName("medianLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.medianLabel)
        self.medianLineEdit = QtWidgets.QLineEdit(self.basicTab)
        self.medianLineEdit.setReadOnly(True)
        self.medianLineEdit.setObjectName("medianLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.medianLineEdit)
        self.standardDeviationLabel = QtWidgets.QLabel(self.basicTab)
        self.standardDeviationLabel.setObjectName("standardDeviationLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.standardDeviationLabel)
        self.standardDeviationLineEdit = QtWidgets.QLineEdit(self.basicTab)
        self.standardDeviationLineEdit.setReadOnly(True)
        self.standardDeviationLineEdit.setObjectName("standardDeviationLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.standardDeviationLineEdit)
        self.totalLabel = QtWidgets.QLabel(self.basicTab)
        self.totalLabel.setObjectName("totalLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.totalLabel)
        self.totalLineEdit = QtWidgets.QLineEdit(self.basicTab)
        self.totalLineEdit.setReadOnly(True)
        self.totalLineEdit.setObjectName("totalLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.totalLineEdit)
        self.dataPointCountLabel = QtWidgets.QLabel(self.basicTab)
        self.dataPointCountLabel.setObjectName("dataPointCountLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dataPointCountLabel)
        self.dataPointCountLineEdit = QtWidgets.QLineEdit(self.basicTab)
        self.dataPointCountLineEdit.setReadOnly(True)
        self.dataPointCountLineEdit.setObjectName("dataPointCountLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dataPointCountLineEdit)
        self.verticalLayout_10.addLayout(self.formLayout_2)
        self.tabWidget.addTab(self.basicTab, "")
        self.measuredTab = QtWidgets.QWidget()
        self.measuredTab.setObjectName("measuredTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.measuredTab)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(1, 1, 1, 1)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.equivalentWidthLabel = QtWidgets.QLabel(self.measuredTab)
        self.equivalentWidthLabel.setObjectName("equivalentWidthLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.equivalentWidthLabel)
        self.equivalentWidthLineEdit = QtWidgets.QLineEdit(self.measuredTab)
        self.equivalentWidthLineEdit.setReadOnly(True)
        self.equivalentWidthLineEdit.setObjectName("equivalentWidthLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.equivalentWidthLineEdit)
        self.centroidLabel = QtWidgets.QLabel(self.measuredTab)
        self.centroidLabel.setEnabled(False)
        self.centroidLabel.setObjectName("centroidLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.centroidLabel)
        self.centroidLineEdit = QtWidgets.QLineEdit(self.measuredTab)
        self.centroidLineEdit.setEnabled(False)
        self.centroidLineEdit.setReadOnly(True)
        self.centroidLineEdit.setObjectName("centroidLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.centroidLineEdit)
        self.verticalLayout_9.addLayout(self.formLayout)
        self.tabWidget.addTab(self.measuredTab, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.dockWidgetContents_3)
        self.treeWidget_2.setAnimated(False)
        self.treeWidget_2.setHeaderHidden(True)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_6 = QtWidgets.QToolButton(self.dockWidgetContents_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/Stanley Knife-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_6.setIcon(icon3)
        self.toolButton_6.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_3.addWidget(self.toolButton_6)
        self.arithmeticToolButton = QtWidgets.QToolButton(self.dockWidgetContents_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/Math-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/Math-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arithmeticToolButton.setIcon(icon4)
        self.arithmeticToolButton.setIconSize(QtCore.QSize(20, 20))
        self.arithmeticToolButton.setObjectName("arithmeticToolButton")
        self.horizontalLayout_3.addWidget(self.arithmeticToolButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.layerRemoveButton = QtWidgets.QToolButton(self.dockWidgetContents_3)
        self.layerRemoveButton.setIcon(icon2)
        self.layerRemoveButton.setIconSize(QtCore.QSize(20, 20))
        self.layerRemoveButton.setObjectName("layerRemoveButton")
        self.horizontalLayout_3.addWidget(self.layerRemoveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setMinimumSize(QtCore.QSize(76, 98))
        self.dockWidget_4.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_4)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -152, 306, 476))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.modelsComboBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelsComboBox.sizePolicy().hasHeightForWidth())
        self.modelsComboBox.setSizePolicy(sizePolicy)
        self.modelsComboBox.setObjectName("modelsComboBox")
        self.horizontalLayout.addWidget(self.modelsComboBox)
        self.addModelButton = QtWidgets.QPushButton(self.groupBox)
        self.addModelButton.setObjectName("addModelButton")
        self.horizontalLayout.addWidget(self.addModelButton)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_3)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(130)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.saveModelButton = QtWidgets.QPushButton(self.groupBox_3)
        self.saveModelButton.setEnabled(False)
        self.saveModelButton.setObjectName("saveModelButton")
        self.horizontalLayout_5.addWidget(self.saveModelButton)
        self.loadModelButton = QtWidgets.QPushButton(self.groupBox_3)
        self.loadModelButton.setObjectName("loadModelButton")
        self.horizontalLayout_5.addWidget(self.loadModelButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.fittingRoutinesGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.fittingRoutinesGroupBox.setEnabled(False)
        self.fittingRoutinesGroupBox.setObjectName("fittingRoutinesGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fittingRoutinesGroupBox)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fittingRoutinesComboBox = QtWidgets.QComboBox(self.fittingRoutinesGroupBox)
        self.fittingRoutinesComboBox.setObjectName("fittingRoutinesComboBox")
        self.verticalLayout_6.addWidget(self.fittingRoutinesComboBox)
        self.fitModelLayerButton = QtWidgets.QPushButton(self.fittingRoutinesGroupBox)
        self.fitModelLayerButton.setObjectName("fitModelLayerButton")
        self.verticalLayout_6.addWidget(self.fitModelLayerButton)
        self.verticalLayout_8.addWidget(self.fittingRoutinesGroupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.createModelLayerButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.createModelLayerButton.setObjectName("createModelLayerButton")
        self.horizontalLayout_4.addWidget(self.createModelLayerButton)
        self.updateModelLayerButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.updateModelLayerButton.setObjectName("updateModelLayerButton")
        self.horizontalLayout_4.addWidget(self.updateModelLayerButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_4)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/Open Folder-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon5)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionChange_Color = QtWidgets.QAction(MainWindow)
        self.actionChange_Color.setObjectName("actionChange_Color")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuDocks.menuAction())
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyfocal"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuDocks.setTitle(_translate("MainWindow", "Docks"))
        self.toolButton_3.setToolTip(_translate("MainWindow", "Create new plot window from data"))
        self.toolButton_2.setToolTip(_translate("MainWindow", "Add data to current plot window"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.dataRemoveButton.setToolTip(_translate("MainWindow", "Remove selected data"))
        self.dataRemoveButton.setText(_translate("MainWindow", "..."))
        self.currentLayerLabel.setText(_translate("MainWindow", "Current layer"))
        self.meanLabel.setText(_translate("MainWindow", "Mean"))
        self.medianLabel.setText(_translate("MainWindow", "Median"))
        self.standardDeviationLabel.setText(_translate("MainWindow", "Standard deviation"))
        self.totalLabel.setText(_translate("MainWindow", "Total"))
        self.dataPointCountLabel.setText(_translate("MainWindow", "Data point count"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basicTab), _translate("MainWindow", "Basic"))
        self.equivalentWidthLabel.setText(_translate("MainWindow", "Equivalent width"))
        self.centroidLabel.setText(_translate("MainWindow", "Centroid"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measuredTab), _translate("MainWindow", "Measured"))
        self.dockWidget_3.setWindowTitle(_translate("MainWindow", "Layers"))
        self.toolButton_6.setToolTip(_translate("MainWindow", "Slice the current layer with active ROIs to create a new layer"))
        self.toolButton_6.setText(_translate("MainWindow", "Slice"))
        self.arithmeticToolButton.setToolTip(_translate("MainWindow", "Perform layer arithmetic"))
        self.arithmeticToolButton.setText(_translate("MainWindow", "Layer Arithmetic"))
        self.layerRemoveButton.setToolTip(_translate("MainWindow", "Remove selected layer"))
        self.layerRemoveButton.setText(_translate("MainWindow", "Remove Layer"))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "Model Fitting"))
        self.groupBox.setTitle(_translate("MainWindow", "Add Model"))
        self.addModelButton.setText(_translate("MainWindow", "Select"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Current Models"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Arithmetic Behavior"))
        self.saveModelButton.setText(_translate("MainWindow", "Save"))
        self.loadModelButton.setText(_translate("MainWindow", "Load"))
        self.fittingRoutinesGroupBox.setTitle(_translate("MainWindow", "Fitting Routine"))
        self.fitModelLayerButton.setText(_translate("MainWindow", "Perform Fit"))
        self.createModelLayerButton.setText(_translate("MainWindow", "Create Layer"))
        self.updateModelLayerButton.setText(_translate("MainWindow", "Update Layer"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionRemove.setToolTip(_translate("MainWindow", "Removes the selected layer"))
        self.actionChange_Color.setText(_translate("MainWindow", "Change Color"))
        self.actionChange_Color.setToolTip(_translate("MainWindow", "Change the line color selected layer"))

from . import icon_resource_rc
