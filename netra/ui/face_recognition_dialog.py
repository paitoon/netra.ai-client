from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import cv2
from .ui_face_recognition import Ui_FaceRecognitionDialog
from .camera_chooser_dialog import CameraChooserDialog
from netra.face_recognition_camera import FaceRecognitionCamera

class FaceRecognitionDialog(QDialog):
    def __init__(self, parent=None):
        super(FaceRecognitionDialog, self).__init__(parent)
        self.ui = Ui_FaceRecognitionDialog()
        self.ui.setupUi(self)

        self.ui.imagePushButton.clicked.connect(self.imagePushButtonClicked)
        self.ui.connectPushButton.clicked.connect(self.connectPushButtonClicked)
        self.ui.startPushButton.clicked.connect(self.startPushButtonClicked)
        self.ui.stopPushButton.clicked.connect(self.stopPushButtonClicked)

        self.camera = None

    def closeEvent(self, evt):
        if self.camera:
            self.camera.close()
        
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

        self.ui.imageLabel.setPixmap(QPixmap.fromImage(img))

    def imagePushButtonClicked(self):
        imageFilePath, _ = QFileDialog.getOpenFileName(self, caption='Select image file')
        
        if imageFilePath:
            image = cv2.imread(imageFilePath)
            self.showImage(image)
    
    def connectPushButtonClicked(self):
        cameraType, cameraURI = CameraChooserDialog.getCamera(self)
        self.ui.cameraLineEdit.setText(cameraType + ':' + cameraURI)
        self.camera = FaceRecognitionCamera(cameraType, cameraURI)
        self.camera.setImageContainer(self.ui.imageLabel)
        self.camera.setRecognizedListContainer(self.ui.recognizedListWidget)
        self.camera.start()
        
    def startPushButtonClicked(self):
        self.camera.setGroupName(self.ui.groupLineEdit.text())
        self.camera.setEyeBlinkDetect(self.ui.eyeBlinkCheckBox.isChecked())
        self.camera.startCapture()
        
    def stopPushButtonClicked(self):
        self.camera.stopCapture()
    