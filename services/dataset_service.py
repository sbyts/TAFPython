from client.http_client import HttpClient


class DatasetService:
    def __init__(self, client: HttpClient):
        self.client = client

    def get_datasets(self):
        return self.client.get('datasets')

    def healthcheck(self):
        return self.client.get('healthcheck')

