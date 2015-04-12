import os
import requests
from Framework import OriginalClass
import json

__author__ = 'Brandon'


class GetConnect:

    def __init__(self, **kwargs):

        try:
            self.response = requests.get(kwargs['url'], headers=json.loads(kwargs['headers']))
        except requests.ConnectionError as rqce:
            print(str(rqce))

    def show_response(self, **kwargs):

        if not kwargs:
            response = self.response.json()
            return response
        else:
            response = self.response.json()
            return response['headers'][kwargs['key']]


if __name__ == "__main__":

    myvar = OriginalClass(os.getcwd()+'/test.cfg')

    base_url = myvar.get_base()
    endpoint_url = myvar.get_endpoints("headers")

    request_url = str(base_url) + str(endpoint_url)
    headers = myvar.get_headers()


    myvar2 = GetConnect(url=request_url, headers=headers)

    print(myvar2.show_response(key="Content-Type"))




