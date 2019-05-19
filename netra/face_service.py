import logging
from requests.exceptions import RequestException
from .http_method import HttpMethod
log = logging.getLogger(__name__)
    
class FaceService:
    def __init__(self, netraClient):
        self.netraClient =  netraClient
        self.rootUri = "face"

    def detect(self, imageFilePathName, threshold=0.0, attributes=None):
        uri = self.rootUri + "/detect"

        parameters = {}
        if threshold > 0.0:
            parameters['threshold'] = str(threshold)
        if attributes:
            parameters['attributes'] = attributes
        
        files = { 'image': open(imageFilePathName, 'rb') }

        result = self.netraClient.request(uri, HttpMethod.PUT, files=files, data=parameters)
        log.info(result)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def recognize(self, imageFilePathName, groupName, candidates=0, confidence=0.0, faceLocations=None):
        uri = self.rootUri + "/recognize"

        parameters = { 'groupName': groupName }
        if candidates > 0:
            parameters['candidates'] = str(candidates)
        if confidence > 0.0:
            parameters['confidence'] = str(confidence)
        if faceLocations is not None:
            parameters['faceLocations'] = faceLocations

        files = { 'image': open(imageFilePathName, 'rb') }

        result = self.netraClient.request(uri, HttpMethod.PUT, files=files, data=parameters)
        log.info(result)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None
