from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2
from .ui_camera_chooser import Ui_CameraChooserDialog

class CameraChooserDialog(QDialog):
    def __init__(self, parent=None):
        super(CameraChooserDialog, self).__init__(parent)
        self.ui = Ui_CameraChooserDialog()
        self.ui.setupUi(self)

    def radioButtonStateChanged(self, radioButton):
        pass

    @staticmethod
    def getCamera(parent=None):
        dialog = CameraChooserDialog(parent)
        if dialog.exec_():
            if dialog.ui.localCameraRadioButton.isChecked():
                return 'local', dialog.ui.localCameraLineEdit.text()
            if dialog.ui.ipCameraRadioButton.isChecked():
                return 'ip', dialog.ui.ipCameraLineEdit.text()
            else:
                return None, ''
