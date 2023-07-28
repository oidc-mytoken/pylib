# libmytoken

A python library for interacting with a [mytoken server](https://github.com/oidc-mytoken/server).

This is the very first alpha version of the library, which currently only supports obtaining OpenID Connect access
tokens from a mytoken.

## Usage

```python
import libmytoken

at = libmytoken.get_access_token_from_jwt_mytoken(mytoken)

mytoken_server = libmytoken.MytokenServer("https://mytoken.data.kit.edu")
at = mytoken_server.AccessToken.get(mytoken)
full_response = mytoken_server.AccessToken.api_get(mytoken)

```

### Error Handling

The library will raise an exception of type `MytokenError` if something goes wrong.

Error Handling can be done the following way:

```python
try:
    print(libmytoken.get_access_token_from_jwt_mytoken(mytoken))
except libmytoken.MytokenError as e:
    print("ERROR mytoken: {}".format(e))
```

## Installation

`pip install libmytoken`

## License

`libmytoken` is provided under the [MIT License](https://opensource.org/licenses/MIT).

