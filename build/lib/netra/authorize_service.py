import logging
from requests.exceptions import RequestException
from .http_method import HttpMethod

log = logging.getLogger(__name__)

class AuthorizeService:
    def __init__(self, netraClient):
        self.netraClient =  netraClient
        self.rootUri = "auth"

    def register(self, user, password, rePassword, email):
        uri = self.rootUri + "/register"

        parameters = { 'user': user, 'password': password, 'rePassword': rePassword, 'email': email }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def login(self, user, password):
        uri = self.rootUri + "/login"

        parameters = { 'user': user, 'password': password }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None
    
    def logout(self):
        uri = self.rootUri + "/logout"

        parameters = {}

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def changePassword(self, user, password, rePassword):
        uri = self.rootUri + "/changePassword"

        parameters = { 'user': user, 'password': password, 'rePassword': rePassword }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None

    def changeEmail(self, user, email):
        uri = self.rootUri + "/changeEmail"

        parameters = { 'user': user, 'email': email }

        result = self.netraClient.request(uri, HttpMethod.POST, params=parameters)

        if result['errCode'] != 0:
            raise RequestException(result['errMsg'])
        
        if 'data' in result:
            return True, result['data']
        return True, None
