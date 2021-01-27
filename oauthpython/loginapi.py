import requests
import json


class Login:
    def __init__(self, login_id, base_url):
        self.login_id = login_id
        self.base_url = base_url
        self.headers = {'Content-type': 'application/json'}

    def user_login(self, password):
        login_id = self.login_id
        base_url = self.base_url
        headers = self.headers
        data={
            'login_id': login_id,
            'password': password,
            "device": "web"
        }
        req = requests.post(f'{base_url}/api/v1/user/login', headers=headers, data=json.dumps(data))
        return req.json()

    def twofa(self, question_id, answer, twofa_token):
        login_id = self.login_id
        base_url = self.base_url
        headers = self.headers
        data= {
            'login_id': login_id,
            'twofa': [
                {
                    'question_id': question_id,
                    'answer': answer
                }
            ],
            'twofa_token': twofa_token,
            'type': 'PIN'
        }
        req = requests.post(f'{base_url}/api/v1/user/twofa', headers=headers, data=json.dumps(data))
        return req.json()

if __name__ == '__main__':
    login = Login("KP154", "https://cash.basanonline.com/")
    out = login.user_login("Basan@007")
    twofatoken = out['data']['twofa']['twofa_token']
    print(twofatoken)
    out = login.twofa("22", "111111", twofatoken)
    print(out)