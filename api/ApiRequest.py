import requests
from .Constant import EndPoint


def get_request(link, token):
    req = requests.get(EndPoint+link, headers={'x-authorization-token': token})
    return req.json()


def post_request(link, token, data):
    req = requests.post(url=EndPoint+link, headers={'x-authorization-token': token}, data=data)
    return req.json()
