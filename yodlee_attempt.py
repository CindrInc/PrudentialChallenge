#from urllib.request import Request, urlopen
import requests
import json
#[ base url: https://developer.api.yodlee.com/ysl , api version: 1.1 ]

INFO = {
    'CO_BRAND_LOGIN': 'sbCobdcddf2bf509e1bd18aba3e09326e978d8a',
    'CO_BRAND_PASSWORD': "f12a5508-147e-4913-82e8-2c535d9874c0",
    'users': [
        {
            'loginName': 'sbMemd3aa8452551164e8de97c47f19115e4b0a1',
            'password': 'sbMemd3aa8452551164e8de97c47f19115e4b0a1#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemd3aa8452551164e8de97c47f19115e4b0a2',
            'password': 'sbMemd3aa8452551164e8de97c47f19115e4b0a2#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemd3aa8452551164e8de97c47f19115e4b0a3',
            'password': 'sbMemd3aa8452551164e8de97c47f19115e4b0a3#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemd3aa8452551164e8de97c47f19115e4b0a4',
            'password': 'sbMemd3aa8452551164e8de97c47f19115e4b0a4#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemd3aa8452551164e8de97c47f19115e4b0a5',
            'password': 'sbMemd3aa8452551164e8de97c47f19115e4b0a5#123',
            'locale': 'en_US'
        }
    ],
    'session': {},
    'headers': {'Api-Version': '1.1', 'Cobrand-Name': 'restserver', 'Content-Type': 'application/json'}
}

def getCobrandToken():
    data = {
        "cobrand":{
            "cobrandLogin": INFO['CO_BRAND_LOGIN'],
            "cobrandPassword": INFO['CO_BRAND_PASSWORD'],
            "locale":"en_US"
        }
    }

    data_json = json.dumps(data)
    req = requests.post("https://developer.api.yodlee.com/ysl/cobrand/login", headers=INFO['headers'], data=data_json)
    res = req.json()
    INFO['session']["cobSession"] = res["session"]["cobSession"]

def getUserToken():
    data = {
        "user": INFO['users'][0]
    }

    INFO['headers'].update({
        'Authorization': '{cobSession=%s}' % INFO['session']['cobSession']
    })
    print(INFO['headers'])

    data_json = json.dumps(data)
    req = requests.post("https://developer.api.yodlee.com/ysl/user/login", headers=INFO['headers'], data=data_json)
    res = req.json()
    print(res)

getCobrandToken()
getUserToken()
print(INFO['session']["cobSession"])