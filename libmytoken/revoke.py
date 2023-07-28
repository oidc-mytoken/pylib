import requests

from .error import MytokenError


class RevocationEndpoint:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def revoke_id(self, mytoken, mom_id, oidc_issuer=None, recursive=False):
        post_data = {
            "token": mytoken,
            "recursive": recursive,
        }
        if oidc_issuer is not None:
            post_data["oidc_issuer"] = oidc_issuer
        if mom_id is not None:
            post_data["mom_id"] = mom_id

        response = requests.post(self.endpoint, json=post_data)
        resp = response.json()
        if response.status_code >= 400:
            raise MytokenError(resp['error'], resp['error_description'])

    def revoke(self, mytoken, oidc_issuer=None, recursive=False):
        self.revoke_id(mytoken, None, oidc_issuer, recursive)
