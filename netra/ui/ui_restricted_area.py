# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restricted_area.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_restrictedAreaDialog(object):
    def setupUi(self, restrictedAreaDialog):
        restrictedAreaDialog.setObjectName("restrictedAreaDialog")
        restrictedAreaDialog.resize(785, 446)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(restrictedAreaDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveToolButton = QtWidgets.QToolButton(restrictedAreaDialog)
        self.saveToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.saveToolButton.setObjectName("saveToolButton")
        self.horizontalLayout.addWidget(self.saveToolButton)
        self.deleteToolButton = QtWidgets.QToolButton(restrictedAreaDialog)
        self.deleteToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.deleteToolButton.setObjectName("deleteToolButton")
        self.horizontalLayout.addWidget(self.deleteToolButton)
        self.conenctToolButton = QtWidgets.QToolButton(restrictedAreaDialog)
        self.conenctToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.conenctToolButton.setObjectName("conenctToolButton")
        self.horizontalLayout.addWidget(self.conenctToolButton)
        self.cameraLineEdit = QtWidgets.QLineEdit(restrictedAreaDialog)
        self.cameraLineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.cameraLineEdit.setObjectName("cameraLineEdit")
        self.horizontalLayout.addWidget(self.cameraLineEdit)
        self.colorLabel = QtWidgets.QLabel(restrictedAreaDialog)
        self.colorLabel.setMinimumSize(QtCore.QSize(20, 0))
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorLabel.setText("")
        self.colorLabel.setTextFormat(QtCore.Qt.PlainText)
        self.colorLabel.setObjectName("colorLabel")
        self.horizontalLayout.addWidget(self.colorLabel)
        self.colorToolButton = QtWidgets.QToolButton(restrictedAreaDialog)
        self.colorToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.colorToolButton.setObjectName("colorToolButton")
        self.horizontalLayout.addWidget(self.colorToolButton)
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeToolButton = QtWidgets.QToolButton(restrictedAreaDialog)
        self.closeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.closeToolButton.setObjectName("closeToolButton")
        self.horizontalLayout.addWidget(self.closeToolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(restrictedAreaDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 763, 363))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageWidget = NetraImageWidget(self.scrollAreaWidgetContents)
        self.imageWidget.setText("")
        self.imageWidget.setObjectName("imageWidget")
        self.horizontalLayout_2.addWidget(self.imageWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.statusLabel = QtWidgets.QLabel(restrictedAreaDialog)
        self.statusLabel.setMinimumSize(QtCore.QSize(0, 24))
        self.statusLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_2.addWidget(self.statusLabel)

        self.retranslateUi(restrictedAreaDialog)
        QtCore.QMetaObject.connectSlotsByName(restrictedAreaDialog)

    def retranslateUi(self, restrictedAreaDialog):
        _translate = QtCore.QCoreApplication.translate
        restrictedAreaDialog.setWindowTitle(_translate("restrictedAreaDialog", "Define Restricted Area"))
        self.saveToolButton.setText(_translate("restrictedAreaDialog", "Save"))
        self.deleteToolButton.setText(_translate("restrictedAreaDialog", "Delete"))
        self.conenctToolButton.setText(_translate("restrictedAreaDialog", "Connect"))
        self.cameraLineEdit.setText(_translate("restrictedAreaDialog", "0"))
        self.colorToolButton.setText(_translate("restrictedAreaDialog", "Color"))
        self.closeToolButton.setText(_translate("restrictedAreaDialog", "Close"))


from .netra_image_widget import NetraImageWidget
