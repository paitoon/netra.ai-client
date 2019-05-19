# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_recognition.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceRecognitionDialog(object):
    def setupUi(self, FaceRecognitionDialog):
        FaceRecognitionDialog.setObjectName("FaceRecognitionDialog")
        FaceRecognitionDialog.resize(969, 605)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(FaceRecognitionDialog)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imagePushButton = QtWidgets.QPushButton(FaceRecognitionDialog)
        self.imagePushButton.setObjectName("imagePushButton")
        self.horizontalLayout.addWidget(self.imagePushButton)
        self.connectPushButton = QtWidgets.QPushButton(FaceRecognitionDialog)
        self.connectPushButton.setObjectName("connectPushButton")
        self.horizontalLayout.addWidget(self.connectPushButton)
        self.cameraLineEdit = QtWidgets.QLineEdit(FaceRecognitionDialog)
        self.cameraLineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.cameraLineEdit.setObjectName("cameraLineEdit")
        self.horizontalLayout.addWidget(self.cameraLineEdit)
        self.label = QtWidgets.QLabel(FaceRecognitionDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.groupLineEdit = QtWidgets.QLineEdit(FaceRecognitionDialog)
        self.groupLineEdit.setObjectName("groupLineEdit")
        self.horizontalLayout.addWidget(self.groupLineEdit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.eyeBlinkCheckBox = QtWidgets.QCheckBox(FaceRecognitionDialog)
        self.eyeBlinkCheckBox.setObjectName("eyeBlinkCheckBox")
        self.horizontalLayout_4.addWidget(self.eyeBlinkCheckBox)
        spacerItem = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startPushButton = QtWidgets.QPushButton(FaceRecognitionDialog)
        self.startPushButton.setMinimumSize(QtCore.QSize(40, 0))
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout_3.addWidget(self.startPushButton)
        self.stopPushButton = QtWidgets.QPushButton(FaceRecognitionDialog)
        self.stopPushButton.setMinimumSize(QtCore.QSize(40, 0))
        self.stopPushButton.setObjectName("stopPushButton")
        self.horizontalLayout_3.addWidget(self.stopPushButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(FaceRecognitionDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 464, 525))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setMinimumSize(QtCore.QSize(64, 48))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_2.addWidget(self.imageLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.scrollArea)
        self.recognizedListWidget = QtWidgets.QListWidget(FaceRecognitionDialog)
        self.recognizedListWidget.setObjectName("recognizedListWidget")
        self.horizontalLayout_5.addWidget(self.recognizedListWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(FaceRecognitionDialog)
        QtCore.QMetaObject.connectSlotsByName(FaceRecognitionDialog)

    def retranslateUi(self, FaceRecognitionDialog):
        _translate = QtCore.QCoreApplication.translate
        FaceRecognitionDialog.setWindowTitle(_translate("FaceRecognitionDialog", "Face Recognition"))
        self.imagePushButton.setText(_translate("FaceRecognitionDialog", "Image"))
        self.connectPushButton.setText(_translate("FaceRecognitionDialog", "Connect"))
        self.cameraLineEdit.setText(_translate("FaceRecognitionDialog", "0"))
        self.label.setText(_translate("FaceRecognitionDialog", "Group : "))
        self.groupLineEdit.setText(_translate("FaceRecognitionDialog", "g-able"))
        self.eyeBlinkCheckBox.setText(_translate("FaceRecognitionDialog", "Eye Blink"))
        self.startPushButton.setText(_translate("FaceRecognitionDialog", "Start"))
        self.stopPushButton.setText(_translate("FaceRecognitionDialog", "Stop"))


