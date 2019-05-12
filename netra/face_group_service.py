import os
import logging
from requests.exceptions import RequestException
from .http_method import HttpMethod

log = logging.getLogger(__name__)
    
class FaceGroupService:
    def __init__(self, netraClient):
        self.netraClient =  netraClient
        self.rootUri = "face/group"

    def get(self, groupName):
        uri = self.rootUri + "/get"

        parameters = { 'groupName': groupName }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def list(self):
        uri = self.rootUri + "/list"

        parameters = {}

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def create(self, groupName):
        uri = self.rootUri + "/create"

        parameters = { 'groupName': groupName }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def delete(self, groupName):
        uri = self.rootUri + "/delete"

        parameters = { 'groupName': groupName }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def upload(self, groupName, personName, imagePathNames):
        uri = self.rootUri + "/upload"

        parameters = { 'groupName': groupName, 'personName': personName }

        files = []
        for n, imagePathName in enumerate(imagePathNames):
            files.append(('file'+str(n+1), open(imagePathName, 'rb')))
 
        result = self.netraClient.request(uri, HttpMethod.PUT, files=files, data=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def train(self, groupName, isForced=False):
        uri = self.rootUri + "/train"

        parameters = { 'groupName': groupName, 'isForced': isForced }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def getTrainStatus(self, groupName):
        uri = self.rootUri + "/getTrainStatus"

        parameters = { 'groupName': groupName }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

