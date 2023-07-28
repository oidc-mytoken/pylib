import jwt

from .error import MytokenError
from .server import get_mytoken_server


def get_access_token_from_jwt_mytoken(mytoken, scopes=None, audiences=None, comment=None):
    token_data = jwt.decode(mytoken, options={"verify_signature": False})
    url = token_data['iss']
    if url is None:
        raise MytokenError("could not get mytoken server from mytoken")
    mytoken_server = get_mytoken_server(url)
    return mytoken_server.AccessToken.get(mytoken, scopes=scopes, audiences=audiences, comment=comment)
