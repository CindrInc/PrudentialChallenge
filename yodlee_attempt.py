import requests
import json
INFO = {
    'CO_BRAND_LOGIN': 'sbCobdcddf2bf509e1bd18aba3e09326e978d8a',
    'CO_BRAND_PASSWORD': "f12a5508-147e-4913-82e8-2c535d9874c0",
    'users': [
        {
            'loginName': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a1',
            'password': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a1#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a2',
            'password': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a2#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a3',
            'password': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a3#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a4',
            'password': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a4#123',
            'locale': 'en_US'
        },
        {
            'loginName': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a5',
            'password': 'sbMemdcddf2bf509e1bd18aba3e09326e978d8a5#123',
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
    req = requests.post("https://developer.api.yodlee.com/ysl/cobrand/login", headers=INFO['headers'], data=json.dumps(data))
    res = req.json()
    INFO['session']["cobSession"] = res["session"]["cobSession"]
    INFO['headers'].update({
        'Authorization': '{cobSession=%s}' % INFO['session']['cobSession']
    })

def getUserToken(user):
    data = {
        "user": user
    }
    req = requests.post("https://developer.api.yodlee.com/ysl/user/login", headers=INFO['headers'], data=json.dumps(data))
    res = req.json()
    INFO['session']["userSession"] = res['user']["session"]["userSession"]
    INFO['headers'].update({
        'Authorization': '{cobSession=%s,userSession=%s}' % (INFO['session']['cobSession'], INFO['session']['userSession'])
    })

def getAccounts():
    req = requests.get("https://developer.api.yodlee.com/ysl/accounts", headers=INFO['headers'])
    return req.json()['account']

def printTransactionCategories():
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/categories", headers=INFO['headers'])
    print(json.dumps(req.json(), indent=4))

def getTransactions(account):
    data = {
        # "container": "creditCard",
        # "accountId": account['id'],
        "fromDate": "2000-01-01",
        "toDate": "2020-01-01"
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions", headers=INFO['headers'], params=data)
    return req.json()

def getTransactionsCount(account):
    data = {
        "fromDate": "2000-01-01",
        "toDate": "2020-01-01"
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/count", headers=INFO['headers'], params=data)
    return req.json()

getCobrandToken()
getUserToken(INFO['users'][0])
# printTransactionCategories()
accounts = getAccounts()
# for account in accounts:
#     print(json.dumps(getTransactions(account), indent=4))
print(json.dumps(getTransactions(accounts[0]), indent=4))
print(json.dumps(getTransactionsCount(accounts[0]), indent=4))