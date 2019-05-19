import os
import logging
from requests.exceptions import RequestException
from .http_method import HttpMethod

log = logging.getLogger(__name__)

class ObjectDetectionService:
    def __init__(self, netraClient):
        self.netraClient =  netraClient
        self.rootUri = "object"

    def getKnownObjects(self):
        uri = self.rootUri + "/getKnownObjects"

        parameters = {}

        result = self.netraClient.request(uri, HttpMethod.POST, parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def detect(self, imageFilePathName, threshold=0.0, interestedObjects=None):
        uri = self.rootUri + "/detect"

        parameters = { 'threshold': str(threshold), 'interestedObjects': interestedObjects }
        files = { 'image': open(imageFilePathName, 'rb') }

        result = self.netraClient.request(uri, HttpMethod.PUT, files=files, data=parameters)
        log.info(result)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None
