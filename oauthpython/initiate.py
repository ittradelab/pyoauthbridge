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

    def put_request(self, url, data):
        headers = self.headers
        headers['x-authorization-token'] = self.token
        res = requests.put(f'{self.base_url}{url}', headers=headers, data=json.dumps(data))
        print(res)
        return res.json()

    def delete_request(self, url, params):
        headers = self.headers
        headers['x-authorization-token'] = self.token
        res = requests.delete(f'{self.base_url}{url}' , params=params, headers=headers)
        return res.json()

    def profile(self, payload):
        params = {'client_id': payload.client_id}
        res = self.get_request("/api/v1/user/profile", params)
        return res

    def place_normal_order(self, payload):
        data = {
            "exchange": payload.exchange,
            "instrument_token": payload.instrument_token,
            "client_id": payload.client_id,
            "order_type": payload.order_type,
            "amo": payload.amo,
            "price": payload.price,
            "quantity": payload.quantity,
            "disclosed_quantity": payload.disclosed_quantity,
            "validity": payload.validity,
            "product": payload.product,
            "order_side": payload.order_side,
            "device": "api",
            "user_order_id": payload.user_order_id,
            "trigger_price": payload.tigger_price,
            "execution_type": payload.execution_type
        }
        res = self.post_request(f'/api/v1/orders', data)
        return res

    def modify_orders(self, payload):
        data = {
            "exchange": payload.exchange,
            "instrument_token": payload.instrument_token,
            "client_id": payload.client_id,
            "order_type": payload.order_type,
            "price": payload.price,
            "quantity": payload.quantity,
            "disclosed_quantity": payload.disclosed_quantity,
            "validity": payload.validity,
            "product": payload.product,
            "oms_order_id": payload.oms_order_id,
            "trigger_price": payload.trigger_price,
            "execution_type": payload.execution_type
        }
        res = self.put_request("/api/v1/orders", data)
        return res

    def cancel_orders(self, payload):
        params = {
            'client_id': payload.client_id,
            'execution_type': payload.execution_type
        }
        res = self.delete_request(f'/api/v1/orders/{payload.oms_order_id}', params)
        return res

    def scripinfo(self, payload):
        params = {
            'info': 'scrip',
            'token': payload.token
        }
        res = self.get_request(f'/api/v1/contract/NSE', params)
        return res

    def search_script(self, payload):
        params = {
            'key': payload.key
        }
        res = self.get_request(f'/api/v1/search', params)
        return res

    def fetch_pending_orders(self, payload):
        params = {
            'type': 'pending',
            'client_id': payload.client_id
        }
        res = self.get_request(f'/api/v1/orders', params)
        return res

    def fetch_completed_orders(self, payload):
        params = {
            'type': 'completed',
            'client_id': payload.client_id
        }
        res = self.get_request(f'/api/v1/orders', params)
        return res

    def trade_book(self, payload):
        params = {
            'client_id': payload.client_id
        }
        res = self.get_request(f'/api/v1/trades', params)
        return res

    def order_history(self, payload):
        params = {
            'client_id': payload.client_id
        }
        res = self.get_request(f'/api/v1/order/{payload.oms_order_id}/history', params)
        return res

    def fetch_live_position(self, payload):
        params = {
            'client_id': payload.client_id,
            'type': 'live'
        }
        res = self.get_request(f'/api/v1/positions', params)
        return res

    def fetch_netwise_position(self, payload):
        params = {
            'client_id': payload.client_id,
            'type': 'historical'
        }
        res = self.get_request(f'/api/v1/positions', params)
        return res

    def fetch_demat_holding(self, payload):
        params = {
            'client_id': payload.client_id
        }
        res = self.get_request(f'/api/v1/holdings', params)
        return res

    def fetch_funds_v2(self, payload):
        params = {
            'client_id': payload.client_id,
            'type': 'all'
        }
        res = self.get_request(f'/api/v2/funds/view', params)
        return res

    def fetch_funds_v1(self, payload):
        params = {
            'client_id': payload.client_id,
            'type': 'all'
        }
        res = self.get_request(f'/api/v1/funds/view', params)
        return res

    def create_alert(self, payload):
        data = {
            'exchange': payload.exchange,
            'instrument_token': payload.instrument_token,
            'wait_time': payload.wait_time,
            'condition': payload.condition,
            'user_set_values': payload.user_set_values,
            'frequency': payload.frequency,
            'expiry': payload.expiry,
            'state_after_expiry': payload.state_after_expiry,
            'user_message': payload.user_message
        }
        res = self.post_request(f'/api/v1/alerts', data)
        return res

    def fetch_alert(self):
        params = {}
        res = self.get_request(f'/api/v1/alerts', params)
        return res

    def alert_update(self, payload):
        data = {
            'exchange': payload.exchange,
            'instrument_token': payload.instrument_token,
            'wait_time': payload.wait_time,
            'condition': payload.condition,
            'user_set_values': payload.user_set_values,
            'frequency': payload.frequency,
            'expiry': payload.expiry,
            'state_after_expiry': payload.state_after_expiry,
            'user_message': payload.user_message
        }
        res = self.put_request(f'/api/v1/alerts', data)
        return res

if __name__ == "__main__":
    connect = Initiate("https://mimik.tradelab.in")
    token_json = connect.user_login("SATYAM", "Trade@321")
    token = token_json['data']['twofa']['twofa_token']
    token_json = connect.twofa("22", "123456", token)
    auth_token = token_json['data']['auth_token']
    connect.set_token(auth_token)
    print(auth_token)
    res = connect.modify_orders()
    print(res)