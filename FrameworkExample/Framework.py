from configparser import RawConfigParser
import os

__author__ = 'Brandon'

class OriginalClass:

    def __init__(self, config):
        self.config = RawConfigParser()
        self.config.read(config)
        self.endpoints = self.config.options("Endpoints")

    def get_headers(self):
        header = self.config.get("Headers", "json")
        return header


    def get_base(self):
        base = self.config.get("Base", "base")
        return base

    def get_endpoints(self, endpoints):

        for section_keys in self.endpoints:
            if section_keys == endpoints:
                endpoint_object = self.config.get("Endpoints", endpoints)

                return endpoint_object






    #def get_queries(self, ):


if __name__ == "__main__":

    myvar = OriginalClass(os.getcwd()+'/test.cfg')

    base = myvar.get_base()

    endpoint = myvar.get_endpoints("headers")

    request_url = str(base)+str(endpoint)

    print(request_url)