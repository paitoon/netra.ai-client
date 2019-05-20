import threading
import time
from datetime import datetime
from multiprocessing import Queue
import cv2
import json
import tempfile
import logging
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QListWidget
from .face_detector import FaceDetector
from .client import NetraClient

log = logging.getLogger(__name__)

class ObjectDetectionCamera(threading.Thread):
    def __init__(self, cameraType='local', uri='0'):
        threading.Thread.__init__(self)

        self.cameraType = 'local'
        self.uri = uri
        self.groupName = ''
        self.eyeBlinkDetect = False

        self.VIDEO_STREAM = "http://%s/videostream.cgi?user=admin&pwd=%s"
        self.SET_RESOLUTION = "http://%s/camera_control.cgi?param=%d&value=%d&user=admin&pwd=%s"
        self.SET_PT = "http://%s/decoder_control.cgi?command=%d&onestep=0&user=admin&pwd=%s"

        self.VGA_RESOLUTION = 0
        self.QVGA_RESOLUTION = 1

        self.PTZ_UP = 0
        self.PTZ_UP_STOP = 1
        self.PTZ_DOWN = 2
        self.PTZ_DOWN_STOP = 3
        self.PTZ_LEFT = 4
        self.PTZ_LEFT_STOP = 5
        self.PTZ_RIGHT = 6
        self.PTZ_RIGHT_STOP = 7
        self.PTZ_LEFT_UP = 90
        self.PTZ_RIGHT_UP = 91
        self.PTZ_LEFT_DOWN = 92
        self.PTZ_RIGHT_DOWN = 93
        self.PTZ_CENTER = 25
        self.PTZ_STOP = 1

        self.fps = 0
        self.cameraFps = 0
        self.frameWidth = 0
        self.frameHeight = 0
        self.codec = 0

        self.running = False
        self.capture = False

        self.imageContainer = QLabel()
        self.recognizedListContainer = QListWidget()

        #self.VIDEO_STREAM = "http://{}/videostream.cgi?user={}&pwd={}"
        self.videoIn = cv2.VideoCapture()

        self.faceDetector = FaceDetector()

        self.netraClient = NetraClient.getInstance()
        self.faceService = self.netraClient.getFaceService()

    def run(self):
        log.info("Camera : {}:{} was started...".format(self.cameraType, self.name))
        
        if self.cameraType.lower() == 'local':
            cameraNo = int(self.uri)
            log.info("Open local camera no. : {}".format(cameraNo))
            self.videoIn.open(cameraNo)
        elif self.cameraType.lower() == 'remote':
            log.info("Open remote cameara : '{}'".format(self.uri))
            self.videoIn.open(self.uri)

        self.cameraFps = self.videoIn.get(cv2.CAP_PROP_FPS)
        self.frameWidth = int(self.videoIn.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frameHeight = int(self.videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.codec = self.videoIn.get(cv2.CAP_PROP_FOURCC)

        if self.fps <= 0 or self.fps > self.cameraFps:
            self.fps = self.cameraFps
        delayInSeconds = 1 / self.fps

        log.info("camera fps={}, frameWidth={}, frameHeight={}, requested fps={}, delay in second={}".format(self.cameraFps, self.frameWidth, self.frameHeight, self.fps, delayInSeconds))

        self.running = True
        while self.running:
            if self.capture:
                grabbed, imageFrame = self.videoIn.read()
                if not grabbed:
                    log.info("End of video...exit.")
                    self.running = False
                    continue

                if self.eyeBlinkDetect:
                    try:
                        markedImage, totalEyeBlink = self.faceDetector.detectEyeBlink(imageFrame)
                        self.showImage(markedImage)
                        if totalEyeBlink <= 0:
                            continue
                        markedImage, faceLocations, status = self.faceDetector.detectFace(imageFrame, True)
                        faceLocationsJson = json.dumps({ 'faceLocations': faceLocations })
                        self.showImage(markedImage)
                        if status:
                            _, imageFilePathName = tempfile.mkstemp(prefix='image', suffix='.jpg')
                            cv2.imwrite(imageFilePathName, imageFrame)
                            status, data = self.faceService.recognize(imageFilePathName, self.groupName, 1, 0.7, faceLocationsJson)
                            if len(data) > 0:
                                candidates = data[0]['candidates']
                                if len(candidates) > 0:
                                    self.recognizedListContainer.addItem("Recognize '{}' identified at : {} with confidence : {}".format(candidates[0]['person'], datetime.now(), candidates[0]['confidence']))
                                    time.sleep(5)
                                    self.faceDetector.resetEyeBlink()
                    except Exception as e:
                        log.error(e)

            time.sleep(delayInSeconds)
        
        log.info("Camera was stopped.")
        self.videoIn.release()

    def close(self):
        self.running = False

    def isRunning(self):
        return self.running

    def startCapture(self):
        log.info('Start capture...')
        self.capture = True
    
    def stopCapture(self):
        log.info('Stop capture...')
        self.capture = False

    def getProcessedInfo(self):
        return { 'fps': self.fps, 'frameWidth': self.frameWidth, 'frameHeight': self.frameHeight }
    
    def setFps(self, fps):
        self.fps = fps

    def setResolution(self, resolution):
        pass

    def setPTZ(self, move_direction, stop_direction):
        pass
    
    def setImageContainer(self, imageContainer):
        self.imageContainer = imageContainer
    
    def setRecognizedListContainer(self, recognizedListContainer):
        self.recognizedListContainer = recognizedListContainer

    def setGroupName(self, groupName):
        self.groupName = groupName
    
    def setEyeBlinkDetect(self, eyeBlink=False):
        self.eyeBlinkDetect = eyeBlink

    def showImage(self, image):
        scaleFactor = self.imageContainer.width() / image.shape[1]
        image = cv2.resize(image, (int(image.shape[1]*scaleFactor), int(image.shape[0]*scaleFactor)))
        
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

        self.imageContainer.setPixmap(QPixmap.fromImage(img))
