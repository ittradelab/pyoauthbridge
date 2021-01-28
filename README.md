# Oauth-Python

Oauth-Python is a official python library to communicate with tradelab api.

### Installation

Oauth-Python requires [python](https://www.python.org/) v3+ to run.

Install the package using pip.

```sh
$ pip install oauth-python
```

### How to use

import package
```sh
$ from oauth-python import Initiate
```
login
```sh
$ connect = Initiate("https://mimik.tradelab.in")
$ token_json = connect.user_login("john", "********")
$ token = token_json['data']['twofa']['twofa_token']
$ token_json = connect.twofa("22", "********", token)
```
set token
```sh
$ auth_token = token_json['data']['auth_token']
$ connect.set_token(auth_token)
```

implementation
```sh
payload = {
    'client_id': 'JOHN'
}
res = connect.profile(payload)
print(res)
```
