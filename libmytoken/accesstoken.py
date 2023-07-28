import requests

from .error import MytokenError


class AccessTokenEndpoint:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def api_get(self, mytoken, oidc_issuer=None, scopes=None, audiences=None, comment=None):
        post_data = {
            "grant_type": "mytoken",
            "mytoken": mytoken,
        }
        if oidc_issuer is not None:
            post_data["oidc_issuer"] = oidc_issuer
        if scopes is not None:
            if type(scopes) is list:
                scopes = " ".join(scopes)
            post_data["scope"] = scopes
        if audiences is not None:
            if type(audiences) is list:
                audiences = " ".join(audiences)
            post_data["audience"] = oidc_issuer
        if comment is not None:
            post_data["comment"] = comment

        response = requests.post(self.endpoint, json=post_data)
        resp = response.json()
        if response.status_code >= 400:
            raise MytokenError(resp['error'], resp['error_description'])
        return resp

    def get(self, mytoken, oidc_issuer=None, scopes=None, audiences=None, comment=None):
        resp = self.api_get(mytoken, oidc_issuer, scopes, audiences, comment)
        # mytoken update is not handled
        return resp['access_token']
