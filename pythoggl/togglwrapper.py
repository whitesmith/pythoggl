from togglexceptions import *
import requests
import base64
import json


class TogglWrapper:
    """
        A simple wrapper for the Toggl API
    """

    TOGGL_URL = 'https://www.toggl.com/api/v8'

    def __init__(self, email=None, password=None, **kwargs):
        if  'api_token' not in kwargs and (email is None or password is None):
            raise NoCredentialsProvided("Please provide either an API token or email and password")

        self.email     = email
        self.password  = password
        self.api_token = None
        if 'api_token' in kwargs: self.api_token = kwargs['api_token']

        if self.api_token is None:
            self.auth = requests.auth.HTTPBasicAuth(self.email,self.password)
        else:
            self.auth = requests.auth.HTTPBasicAuth(self.api_token,'api_token')


    def profile(self):
        return requests.get(self.TOGGL_URL+'/me',auth=self.auth)

    def workspaces(self):
        return requests.get(self.TOGGL_URL+'/workspaces',auth=self.auth)
