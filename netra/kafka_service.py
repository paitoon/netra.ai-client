import os
import logging
from requests.exceptions import RequestException
from .http_method import HttpMethod

log = logging.getLogger(__name__)
    
class KafkaService:
    def __init__(self, netraClient):
        self.netraClient =  netraClient
        self.rootUri = "kafka"

    def get(self):
        uri = self.rootUri + "/get"

        parameters = {}

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def set(self, parameters):
        uri = self.rootUri + "/get"

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None
