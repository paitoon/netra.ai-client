# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/camera_chooser.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraChooserDialog(object):
    def setupUi(self, CameraChooserDialog):
        CameraChooserDialog.setObjectName("CameraChooserDialog")
        CameraChooserDialog.resize(400, 106)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(CameraChooserDialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.localCameraRadioButton = QtWidgets.QRadioButton(CameraChooserDialog)
        self.localCameraRadioButton.setMinimumSize(QtCore.QSize(107, 0))
        self.localCameraRadioButton.setChecked(True)
        self.localCameraRadioButton.setObjectName("localCameraRadioButton")
        self.horizontalLayout.addWidget(self.localCameraRadioButton)
        self.localCameraLineEdit = QtWidgets.QLineEdit(CameraChooserDialog)
        self.localCameraLineEdit.setObjectName("localCameraLineEdit")
        self.horizontalLayout.addWidget(self.localCameraLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ipCameraRadioButton = QtWidgets.QRadioButton(CameraChooserDialog)
        self.ipCameraRadioButton.setMinimumSize(QtCore.QSize(107, 0))
        self.ipCameraRadioButton.setObjectName("ipCameraRadioButton")
        self.horizontalLayout_2.addWidget(self.ipCameraRadioButton)
        self.ipCameraLineEdit = QtWidgets.QLineEdit(CameraChooserDialog)
        self.ipCameraLineEdit.setObjectName("ipCameraLineEdit")
        self.horizontalLayout_2.addWidget(self.ipCameraLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(CameraChooserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(CameraChooserDialog)
        self.buttonBox.accepted.connect(CameraChooserDialog.accept)
        self.buttonBox.rejected.connect(CameraChooserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CameraChooserDialog)

    def retranslateUi(self, CameraChooserDialog):
        _translate = QtCore.QCoreApplication.translate
        CameraChooserDialog.setWindowTitle(_translate("CameraChooserDialog", "Camera Chooser"))
        self.localCameraRadioButton.setText(_translate("CameraChooserDialog", "Local Camera"))
        self.localCameraLineEdit.setText(_translate("CameraChooserDialog", "0"))
        self.ipCameraRadioButton.setText(_translate("CameraChooserDialog", "IP Camera"))


