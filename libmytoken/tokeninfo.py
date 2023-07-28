import requests

from .error import MytokenError


class TokeninfoEndpoint:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def __api(self, data):
        response = requests.post(self.endpoint, json=data)
        resp = response.json()
        if response.status_code >= 400:
            raise MytokenError(resp['error'], resp['error_description'])
        return resp

    def introspect(self, mytoken):
        return self.__api({"action": "introspect", "mytoken": mytoken})

    def api_history(self, mytoken, mom_ids=None):
        post_data = {
            "action": "event_history",
            "mytoken": mytoken,
        }
        if mom_ids is not None:
            if type(mom_ids) is not list:
                mom_ids = [mom_ids]
            post_data["mom_ids"] = mom_ids

        return self.__api(post_data)

    def history(self, mytoken, mom_ids=None):
        resp = self.api_history(mytoken, mom_ids)
        # mytoken update is not handled
        return resp['events']

    def api_subtokens(self, mytoken):
        return self.__api({"action": "subtokens", "mytoken": mytoken})

    def subtokens(self, mytoken):
        resp = self.api_subtokens(mytoken)
        # mytoken update is not handled
        return resp['mytokens']

    def api_list_mytokens(self, mytoken):
        return self.__api({"action": "list_mytokens", "mytoken": mytoken})

    def list_mytokens(self, mytoken):
        resp = self.api_list_mytokens(mytoken)
        # mytoken update is not handled
        return resp['mytokens']
