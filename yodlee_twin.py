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
def userChoice(lst):
    print(lst)
    print("type the one you want to view exactly as you see it")
    return input()
def info_for_transactions():
    containers = ["bank","creditCard", "investment", "insurance", "loan"]
    years = list(range(1900,2031))
    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    print("enter which year you want to start looking from")
    from_year = str(userChoice(years))
    print("enter which year you want to look until")
    to_year = str(userChoice(years))
    print("enter which month you want to start looking from")
    from_month = userChoice(months)
    print("enter which month you want to look until")
    to_month = userChoice(months)
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]
    print("enter which day you want to look from")
    from_day = userChoice(days)
    print("enter which day you want to look until")
    to_day = userChoice(days)
    print("Which container you wish to use")
    containerX = userChoice(containers)
    all_info = (from_year,to_year,from_month,to_month,from_day,to_day,containerX)
    return all_info
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

def getTransactions(account,from_year,to_year,from_month,to_month,from_day,to_day):
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
        "container": "creditCard",
        "accountId": account['id'],
        "fromDate": from_year + "-" + from_month + "-" + from_day,
        "toDate": to_year + "-" + to_month + "-" + to_day
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions", headers=INFO['headers'], params=data)
    return req.json()
def getTransactionsCount(account,from_year,to_year,from_month,to_month,from_day,to_day):
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
        "container": "creditCard",
        "accountId": account['id'],
        "fromDate": from_year + "-" + from_month + "-" + from_day,
        "toDate": to_year + "-" + to_month + "-" + to_day
    }

    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/count",headers= INFO['headers'],params = data)
    return req.json()



#printTransactionCategories()
getCobrandToken()
getUserToken(INFO['users'][0])
accounts = getAccounts()
for account in accounts:
    #account,from_year,to_year,from_month,to_month,from_day,to_day)
    print("Number of transactions: ",getTransactionsCount(account,'1900','2020','01','12','01','28'))
    print("Transactions: ",getTransactions(account,'1900','2020','01','12','01','28'))
'''for i in range(len(INFO['users'])):
    getUserToken(INFO['users'][i])
    accounts = getAccounts()
    for account in accounts:
        print("Number of transactions: ",getTransactionsCount(account))
        print("Transactions: ",getTransactions(account))'''
