import requests
import json


class Initiate:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Content-type': 'application/json'}
        self.token = ""
        self.login_id = ""

    def user_login(self, login_id, password):
        base_url = self.base_url
        headers = self.headers
        self.login_id = login_id
        data={
            'login_id': login_id,
            'password': password,
            "device": "web"
        }
        res = requests.post(f'{base_url}/api/v1/user/login', headers=headers, data=json.dumps(data))
        return res.json()

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
        res = requests.post(f'{base_url}/api/v1/user/twofa', headers=headers, data=json.dumps(data))
        return res.json()

    def set_token(self, token):
        self.token = token

    def print_token(self):
        print(self.token)

    def get_request(self, url, params):
        headers = self.headers
        headers['x-authorization-token'] = self.token
        res = requests.get(f'{self.base_url}{url}' , params=params, headers=headers)
        return res.json()

    def post_request(self, url, data):
        headers = self.headers
        headers['x-authorization-token'] = self.token
        res = requests.post(f'{self.base_url}{url}', headers=headers, data=json.dumps(data))
        print(res)
        return res.json()

    def profile(self, login_id):
        params = {'client_id': login_id}
        res = self.get_request("/api/v1/user/profile", params)
        return res

    def place_normal_order(self, exchange, instrument_token, client_id, order_type, amo, price, quantity, disclosed_quantity, validity, product, order_side, user_order_id, tigger_price, execution_type):
        data = {
            "exchange": exchange,
            "instrument_token": instrument_token,
            "client_id": client_id,
            "order_type": order_type,
            "amo": amo,
            "price": price,
            "quantity": quantity,
            "disclosed_quantity": disclosed_quantity,
            "validity": validity,
            "product": product,
            "order_side": order_side,
            "device": "api",
            "user_order_id": user_order_id,
            "trigger_price": tigger_price,
            "execution_type": execution_type
        }
        res = self.post_request("/api/v1/orders", data)
        return res

if __name__ == "__main__":
    connect = Initiate("https://mimik.tradelab.in")
    token_json = connect.user_login("SATYAM", "Trade@321")
    token = token_json['data']['twofa']['twofa_token']
    token_json = connect.twofa("22", "123456", token)
    auth_token = token_json['data']['auth_token']
    connect.set_token(auth_token)
    print(auth_token)
    res = connect.place_normal_order('NSE', 10666, 'SATYAM', 'LIMIT', 'false', 34.8, 1, 0, 'DAY', 'MIS', 'BUY', 10002, 0, 'REGULAR')
    print(res)