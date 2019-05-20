import logging
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QColorDialog
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
import cv2
from .ui_restricted_area import Ui_restrictedAreaDialog

log = logging.getLogger(__name__)

class RestrictedAreaDialog(QDialog):
    def __init__(self, parent=None):
        super(RestrictedAreaDialog, self).__init__(parent)
        self.ui = Ui_restrictedAreaDialog()
        self.ui.setupUi(self)

        self.ui.imageWidget.setMouseTracking(True)
        self.ui.imageWidget.mouseMoved.connect(self.mouseMoved)

        self.ui.saveToolButton.clicked.connect(self.imagePushButtonClicked)
        self.ui.colorToolButton.clicked.connect(self.selectColor)

        self.updateDrawColor(self.ui.imageWidget.drawColor())

        self.camera = None

    def closeEvent(self, evt):
        pass
        #self.camera.close()

    def mouseMoved(self, event):
        self.ui.statusLabel.setText("X={}, Y={}".format(event.pos().x(), event.pos().y()))

    def updateDrawColor(self, color):
        palette = self.ui.colorLabel.palette()
        palette.setColor(self.ui.colorLabel.backgroundRole(), color)
        self.ui.colorLabel.setPalette(palette)

    def showImage(self, image):
        size = image.shape
        step = image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.ui.imageWidget.setPixmap(QPixmap.fromImage(img))

    def imagePushButtonClicked(self):
        imageFilePath, _ = QFileDialog.getOpenFileName(self, caption='Select image file')
        
        if imageFilePath:
            image = cv2.imread(imageFilePath)
            self.showImage(image)

    def selectColor(self):
        color = QColorDialog.getColor()
        self.updateDrawColor(color)
        self.ui.imageWidget.setDrawColor(color)
