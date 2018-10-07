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
    if (req.text.find('err') != -1):
        return False
    INFO['session']["userSession"] = res['user']["session"]["userSession"]
    INFO['headers'].update({
        'Authorization': '{cobSession=%s,userSession=%s}' % (INFO['session']['cobSession'], INFO['session']['userSession'])
    })
    return True

def getAccounts():
    req = requests.get("https://developer.api.yodlee.com/ysl/accounts", headers=INFO['headers'])
    return req.json()['account']

def printTransactionCategories():
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/categories", headers=INFO['headers'])
    print(json.dumps(req.json(), indent=4))

def getTransactions(accountId,from_year,to_year,from_month,to_month,from_day,to_day):
    #all_info = (from_year,to_year,from_month,to_month,from_day,to_day,containerX)
    '''
    info = info_for_transactions()
    print("container: " + info[6])
    print("from_year: " + info[0])
    print("to_year: " + info[1])
    print("from_month: " + info[2])
    print("to_month: " + info[3])
    print("from_day: " + info[4])
    print("to_day: " + info[5])
    data = {
        "container": info[6],
        "accountId": account['id'],
        "fromDate": info[0] + "-" + info[2] + "-" + info[4],
        "toDate": info[1] + "-" + info[3] + "-" + info[5]
    }
    '''
    '''
    data = {
        "container": "creditCard",
        "accountId": account['id'],
        "fromDate": "1900-01-01",
        "toDate": "2030-01-01"
    }
    '''
    data = {
        # "container": "creditCard",
        "accountId": accountId,
        "fromDate": "%d-%02d-%02d" % (from_year, from_month, from_day),
        "toDate": "%d-%02d-%02d" % (to_year, to_month, to_day)
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions", headers=INFO['headers'], params=data)
    return req.json()

def getTransactionsCount(accountId,from_year,to_year,from_month,to_month,from_day,to_day):
    #info = info_for_transactions()
    '''
    print("container: " + info[6])
    print("from_year: " + info[0])
    print("to_year: " + info[1])
    print("from_month: " + info[2])
    print("to_month: " + info[3])
    print("from_day: " + info[4])
    print("to_day: " + info[5])
    print("fromDate: " + info[0] + "-" + info[2] + "-" + info[4])
    print("toDate: " + info[1] + "-" + info[3] + "-" + info[5])
    data = {
        "container": info[6],
        "accountId": account['id'],
        "fromDate": info[0] + "-" + info[2] + "-" + info[4],
        "toDate": info[1] + "-" + info[3] + "-" + info[5]
    }
    '''
    '''
    data = {
        "container": "creditCard",
        "accountId": account['id'],
        "fromDate": "1900-01-01",
        "toDate": "2030-01-01"
    }
    '''
    data = {
        # "container": "creditCard",
        "accountId": accountId,
        "fromDate": "%d-%02d-%02d" % (from_year, from_month, from_day),
        "toDate": "%d-%02d-%02d" % (to_year, to_month, to_day)
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/count", headers=INFO['headers'], params=data)
    return req.json()

def getAccount(accountId):
    accounts = getAccounts()
    for acc in accounts:
        if str(acc['id']) == str(accountId):
            return acc
    return None

def getAllTransactions(accountId):
    return getTransactions(accountId, 1900, 2030, 1, 1, 1, 1)

def init(user):
    return getUserToken(user)


getCobrandToken()
if __name__ == '__main__':
    getCobrandToken()
    getUserToken(INFO['users'][0])
    # printTransactionCategories()
    accounts = getAccounts()
    # for account in accounts:
    #     print(json.dumps(getTransactions(account), indent=4))
    print(json.dumps(getTransactions(accounts[0]['id']), indent=4))
    # print(accounts[0])
    # print(json.dumps(getTransactionsCount(accounts[0]), indent=4))
