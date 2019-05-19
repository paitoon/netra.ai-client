import cv2
import time
from multiprocessing import Queue
import logging
from netra.local_camera import LocalCamera

def newImageFrame(imageFrame):
    cv2.imshow('Image', imageFrame)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)-30.30s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format("log", "netra-ai")),
        logging.StreamHandler()
    ])

log = logging.getLogger(__name__)

inQueue = Queue()
video = LocalCamera('0')
video.setQueue(inQueue)
video.start()
video.startCapture()
while True:
    if inQueue.empty():
        log.info("Object detect processor has no data...wait.")
        time.sleep(1)
        continue
    
    imageFrame = inQueue.get()[0]
    cv2.imshow('Image', imageFrame)

cv2.destroyAllWindows()



