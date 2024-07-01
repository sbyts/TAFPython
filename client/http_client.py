# coding: utf-8
import requests


class HttpClient:
    def __init__(self, host_api_url,
                 auth=None,
                 header=None):
        if header is None:
            header = {'Accepts': 'application/json'}
        self.host_api_url = host_api_url + '/api/v1/'
        self.header = header
        self.auth = auth
        self.client = self.__init_client(header)

    def __init_client(self, header):
        self.session = requests.Session()
        self.session.headers.update(header)
        return self.session

    def get_client(self):
        return self.__init_client(self.header)

    def get(self, operation_id):
        return self.session.get(self.host_api_url + operation_id)
