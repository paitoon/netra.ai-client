import threading
import os
import json
import time
from datetime import datetime, date
import cv2
from multiprocessing import Queue
import logging

log = logging.getLogger(__name__)

class Camera(threading.Thread):
    def __init__(self, uri):

        self.STD_VGA_RESOLUTION = 0
        self.STD_QVGA_RESOLUTION = 1

        self.STD_PTZ_UP = 0
        self.STD_PTZ_UP_STOP = 1
        self.STD_PTZ_DOWN = 2
        self.STD_PTZ_DOWN_STOP = 3
        self.STD_PTZ_LEFT = 4
        self.STD_PTZ_LEFT_STOP = 5
        self.STD_PTZ_RIGHT = 6
        self.STD_PTZ_RIGHT_STOP = 7
        self.STD_PTZ_LEFT_UP = 8
        self.STD_PTZ_RIGHT_UP = 9
        self.STD_PTZ_LEFT_DOWN = 10
        self.STD_PTZ_RIGHT_DOWN = 11
        self.STD_PTZ_CENTER = 12
        self.STD_PTZ_STOP = 13

        self.type = None
        self.uri = uri

        self.fps = 0
        self.cameraFps = 0
        self.frameWidth = 0
        self.frameHeight = 0
        self.codec = 0

        self.running = False
        self.capture = False

        #self.VIDEO_STREAM = "http://{}/videostream.cgi?user={}&pwd={}"
        self.videoIn = cv2.VideoCapture()
        self.newFrameCallback = self.newFrame

    def run(self):
        log.info("Camera : {}:{} was started...".format(self.type, self.name))
        
        if self.type.lower() == 'local':
            cameraNo = int(self.uri)
            log.info("Open local camera no. : {}".format(cameraNo))
            self.videoIn.open(cameraNo)
        elif self.type.lower() == 'remote':
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

                log.info('Fire newFrame event...')
                self.newFrameCallback(imageFrame)

            time.sleep(delayInSeconds)
        
        log.info("Video Procesor was stopped.")
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

    def setnewFrameCallback(self, callback):
        self.newFrameCallback = callback

    def newFrame(self, image):
        pass