from urllib.parse import urljoin

import requests

from .accesstoken import AccessTokenEndpoint
from .error import MytokenError
from .revoke import RevocationEndpoint
from .tokeninfo import TokeninfoEndpoint
from .transfer import TokenTransferEndpoint


class MytokenServer:
    def __init__(self, url):
        config_endpoint = urljoin(url, "/.well-known/mytoken-configuration")
        response = requests.get(config_endpoint)
        if response.status_code != 200:
            raise MytokenError("could not get mytoken configuration", "is the mytoken url '{}' correct?".format(url))
        resp = response.json()
        self.ServerMetadata = resp
        self.AccessToken = AccessTokenEndpoint(resp['access_token_endpoint'])
        # self.Mytoken = MytokenEndpoint(resp['mytoken_endpoint'])
        self.Revocation = RevocationEndpoint(resp['revocation_endpoint'])
        self.Tokeninfo = TokeninfoEndpoint(resp['tokeninfo_endpoint'])
        self.Transfer = TokenTransferEndpoint(resp['token_transfer_endpoint'])


cachedMytokenServers = {}


def get_mytoken_server(url):
    try:
        m = cachedMytokenServers[url]
    except KeyError:
        m = MytokenServer(url)
        cachedMytokenServers[url] = m
    return m
