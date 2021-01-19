from .ApiRequest import get_request, post_request
import json

def login(user_id, password):
    req = post_request("/api/v1/user/login", "", {"login_id": user_id, "password": password, "device": "api"})
    return req


def twofa(login_id, question_id, answer, twofa_token):
    twofaArray = [{"question_id": "22", "answer": "111111"}]
    req = post_request("/api/v1/user/twofa", "", {"login_id": "KP154", "twofa": twofaArray, "twofa_token": "8qcgx8xRcet3M56B9a03gwitOccU1dPBFi0FYL10eSo30Ky4lYISBWlsGzTAOgXWjWt7e4m716qC9dUHnsl1s2Ea004qmQycOYCOsKYVYd0dhDq5OnmTb05N73cSX7GC4299QhDCV5r4oU1xDPQqQT87fwWQoKhKX7pWxFc", "type": "PIN"})
    return req


def userProfile(user_id, token):
    req = get_request("/api/v1/user/profile?client_id="+user_id, token)
    return req
