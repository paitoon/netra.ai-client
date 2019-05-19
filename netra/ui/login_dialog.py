from PyQt5.QtWidgets import QDialog, QMessageBox
from requests.exceptions import RequestException
from .ui_login import Ui_LoginDialog
from ..client import NetraClient

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.login)

        self.netraClient = NetraClient.getInstance()

    def login(self):
        try:
            self.netraClient.connect(self.ui.serverLineEdit.text(), int(self.ui.portLineEdit.text()))
            authorizeService = self.netraClient.getAuthorizeService()
            authorizeService.login(self.ui.userNameLineEdit.text(), self.ui.passwordLineEdit.text())
        except Exception as e:
            print(e)
            QMessageBox.information(self, 'Error', e.args[0])