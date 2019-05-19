import os
import requests
from requests import Session
from requests.exceptions import ConnectionError, RequestException
import json
import logging
from . import netra_crt, netra_key, netra_pem
from .http_method import HttpMethod
from .authorize_service import AuthorizeService
from .face_group_service import FaceGroupService
from .object_detection_service import ObjectDetectionService
from .face_service import FaceService
from .kafka_service import KafkaService

log = logging.getLogger(__name__)

class NetraClient:
    __netraClient = None

    @staticmethod
    def getInstance():
        if NetraClient.__netraClient == None:
            NetraClient.__netraClient = NetraClient()
        return NetraClient.__netraClient

    def __init__(self):
        self.VISION_URI = "/netra/v1.0"
        self.cert = (netra_crt(), netra_key())
        self.pem = netra_pem()
        self.server = None
        self.port = 0
        self.secure = False
        self.baseUrl = ""
        self.session = Session()
        self.authorizeService = None
        self.faceGroupService = None
        self.objectDetectionService = None
        self.faceService = None
        self.kafkaService = None

    def connect(self, server, port, secure=False):
        self.server = server
        self.port = port
        self.secure = secure
        self.baseUrl = "{}://{}:{}{}".format('https', self.server, self.port, self.VISION_URI) if self.secure else "{}://{}:{}{}".format('http', self.server, self.port, self.VISION_URI)

    def isConnect(self):
        if self.server:
            return True
        return False

    def request(self, path, method, params=None, files=None, data=None):
        if not self.isConnect():
            raise ConnectionError('No connection.')

        pathUrl = '/'.join([self.baseUrl, path])

        log.info("request path : {}, params : {}".format(pathUrl, params))

        if self.secure:
            if method.name == 'POST':
                response = requests.post(pathUrl, json=params, files=files, cert=self.cert)
            elif method.name == 'GET':
                response = requests.get(pathUrl, json=params, files=files, cert=self.cert)
            elif method.name == 'PUT':
                response = requests.put(pathUrl, json=params, files=files, cert=self.cert)
            elif method.name == 'DELETE':
                response = requests.delete(pathUrl, json=params, files=files, cert=self.cert)
            else:
                raise RequestException('Invalid http method.')
        else:
            if method.name == 'POST':
                response = self.session.post(pathUrl, json=params, files=files, data=data)
            elif method.name == 'GET':
                response = self.session.get(pathUrl, json=params, files=files, data=data)
            elif method.name == 'PUT':
                response = self.session.put(pathUrl, json=params, files=files, data=data)
            elif method.name == 'DELETE':
                response = self.session.delete(pathUrl, json=params, files=files, data=data)
            else:
                raise RequestException('Invalid http method.')

        result = json.loads(response.text)
        return result

    def getAuthorizeService(self):
        if self.authorizeService is None:
            self.authorizeService = AuthorizeService(self)
        return self.authorizeService

    def getFaceGroupService(self):
        if self.faceGroupService is None:
            self.faceGroupService = FaceGroupService(self)
        return self.faceGroupService
    
    def getObjectDetectionService(self):
        if self.objectDetectionService is None:
            self.objectDetectionService = ObjectDetectionService(self)
        return self.objectDetectionService
    
    def getFaceService(self):
        if self.faceService is None:
            self.faceService = FaceService(self)
        return self.faceService
    
    def getKafkaService(self):
        if self.kafkaService is None:
            self.kafkaService = KafkaService(self)
        return self.kafkaService