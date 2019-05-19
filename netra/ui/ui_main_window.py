# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuParameters = QtWidgets.QMenu(self.menubar)
        self.menuParameters.setObjectName("menuParameters")
        self.menuFace_Recognition = QtWidgets.QMenu(self.menuParameters)
        self.menuFace_Recognition.setObjectName("menuFace_Recognition")
        self.menuConnect = QtWidgets.QMenu(self.menubar)
        self.menuConnect.setObjectName("menuConnect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfidencial_Level = QtWidgets.QAction(MainWindow)
        self.actionConfidencial_Level.setObjectName("actionConfidencial_Level")
        self.actionCandidates = QtWidgets.QAction(MainWindow)
        self.actionCandidates.setObjectName("actionCandidates")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFace_Recognition = QtWidgets.QAction(MainWindow)
        self.actionFace_Recognition.setObjectName("actionFace_Recognition")
        self.menuImage_Processing.addAction(self.actionFace_Recognition)
        self.menuFace_Recognition.addAction(self.actionConfidencial_Level)
        self.menuFace_Recognition.addAction(self.actionCandidates)
        self.menuParameters.addAction(self.menuFace_Recognition.menuAction())
        self.menuConnect.addAction(self.actionLogin)
        self.menuConnect.addSeparator()
        self.menuConnect.addAction(self.actionExit)
        self.menubar.addAction(self.menuConnect.menuAction())
        self.menubar.addAction(self.menuImage_Processing.menuAction())
        self.menubar.addAction(self.menuParameters.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Netra.AI"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuParameters.setTitle(_translate("MainWindow", "Parameters"))
        self.menuFace_Recognition.setTitle(_translate("MainWindow", "Face Recognition"))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect"))
        self.actionConfidencial_Level.setText(_translate("MainWindow", "Confidencial Level"))
        self.actionCandidates.setText(_translate("MainWindow", "Candidates"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFace_Recognition.setText(_translate("MainWindow", "Face Recognition"))


