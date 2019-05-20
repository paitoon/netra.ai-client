from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStyle, QWidget
from netra.ui.ui_main_window import Ui_MainWindow
from netra.ui.login_dialog import LoginDialog
from netra.ui.face_recognition_dialog import FaceRecognitionDialog
from netra.ui.restricted_area_dialog import RestrictedAreaDialog
import logging
from netra.client import NetraClient

log = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionLogin.triggered.connect(self.login)        
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionFace_Recognition.triggered.connect(self.openFaceRecognition)
        self.ui.actionRestricted_Area.triggered.connect(self.detectRestrictedArea)
        self.netraClient = NetraClient.getInstance()

    def closeEvent(self, evt):
        reply = QMessageBox.question(self, 'Exit', 'Do you want to exit?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.netraClient.getAuthorizeService().logout()
            evt.accept()
        else:
            evt.ignore()

    def login(self):
        dialog = LoginDialog(self)
        dialog.show()

    def openFaceRecognition(self):
        dialog = FaceRecognitionDialog(self)
        dialog.show()

    def detectRestrictedArea(self):
        dialog = RestrictedAreaDialog(self)
        dialog.show()