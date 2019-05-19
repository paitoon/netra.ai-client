from scipy.spatial import distance as dist
import cv2
import dlib
import imutils
from imutils import face_utils
import logging
from . import shape_predictor_68_model

log = logging.getLogger(__name__)

class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(shape_predictor_68_model())

        # grab the indexes of the facial landmarks for the left and
        # right eye, respectively
        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        # define two constants, one for the eye aspect ratio to indicate
        # blink and then a second constant for the number of consecutive
        # frames the eye must be below the threshold
        self.EYE_AR_THRESH = 0.22
        self.EYE_AR_CONSEC_FRAMES = 3
        
        # initialize the frame counters and the total number of blinks
        self.COUNTER = 0
        self.TOTAL = 0

    def _eye_aspect_ratio(self, eye):
        # compute the euclidean distances between the two sets of
        # vertical eye landmarks (x, y)-coordinates
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
    
        # compute the euclidean distance between the horizontal
        # eye landmark (x, y)-coordinates
        C = dist.euclidean(eye[0], eye[3])
    
        # compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)
    
        # return the eye aspect ratio
        return ear
    
    def detectEyeBlink(self, image):
        image = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
        # detect faces in the grayscale frame
        rects = self.detector(gray, 0)

        # loop over the face detections
        for rect in rects:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
    
            # extract the left and right eye coordinates, then use the
            # coordinates to compute the eye aspect ratio for both eyes
            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            leftEAR = self._eye_aspect_ratio(leftEye)
            rightEAR = self._eye_aspect_ratio(rightEye)
    
            # average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            # compute the convex hull for the left and right eye, then
            # visualize each of the eyes
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(image, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(image, [rightEyeHull], -1, (0, 255, 0), 1)

            # check to see if the eye aspect ratio is below the blink
            # threshold, and if so, increment the blink frame counter
            log.info('ear = {}'.format(ear))
            if ear < self.EYE_AR_THRESH:
                self.COUNTER += 1
                log.info("below threshold count = {}".format(self.COUNTER))
    
            # otherwise, the eye aspect ratio is not below the blink
            # threshold
            else:
                # if the eyes were closed for a sufficient number of
                # then increment the total number of blinks
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    self.TOTAL += 1
                    log.info("ear below threshold more than consequence, count eye blink = {}".format(self.TOTAL))
    
                # reset the eye frame counter
                self.COUNTER = 0
    
            # draw the total number of blinks on the frame along with
            # the computed eye aspect ratio for the frame
            cv2.putText(image, "Blinks: {}".format(self.TOTAL), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(image, "EAR: {:.2f}".format(ear), (300, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
        return (image, self.TOTAL)
    
    def resetEyeBlink(self):
        self.TOTAL = 0

    def detectFace(self, image, oneFace=False):
        markedImage = image.copy()
        resizedImage = imutils.resize(markedImage, width=320)
        r = markedImage.shape[1] / float(resizedImage.shape[1])
        gray = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
 
        # detect faces in the grayscale frame
        rects = self.detector(gray, 0)

        originRects = []

        if not oneFace:
            status = True
            # loop over the face detections
            for rect in rects:
                left = int(rect.left() * r)
                top = int(rect.top() * r)
                right = int(rect.right() * r)
                bottom = int(rect.bottom() * r)
                cv2.rectangle(markedImage, (left, top), (right, bottom), (0, 255, 0), 2)
                originRects.append({ 'left': left, 'top': top, 'right': right, 'bottom': bottom })
        else:
            status = False
            if len(rects) > 0:
                areas = [(abs(rect.right()-rect.left())*abs(rect.bottom()-rect.top()), rect) for rect in rects]
                areas.sort(reverse=True)

                log.info('Area = ' + str(areas[0][0]))
                color = (0, 0, 255)
                if areas[0][0] > 7000:
                    color = (0, 255, 0)
                    status = True
                rect = areas[0][1]
                left = int(rect.left() * r)
                top = int(rect.top() * r)
                right = int(rect.right() * r)
                bottom = int(rect.bottom() * r)

                cv2.rectangle(markedImage, (left, top), (right, bottom), color, 2)

                originRects = [{'left': left, 'top': top, 'right': right, 'bottom': bottom}]
        return markedImage, originRects, status
