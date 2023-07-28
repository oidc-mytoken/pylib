import requests

from .error import MytokenError


class TokenTransferEndpoint:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def api_create(self, mytoken):
        response = requests.post(self.endpoint, json={"mytoken": mytoken})
        resp = response.json()
        if response.status_code >= 400:
            raise MytokenError(resp['error'], resp['error_description'])
        return resp

    def create(self, mytoken):
        resp = self.api_create(mytoken)
        # mytoken update is not handled
        return resp['transfer_code']
