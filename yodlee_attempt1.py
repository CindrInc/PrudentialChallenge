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

EXPENSES_CATEGORY_ID = [3,9,2,11,14,45,16,104,37,19,33,24,13,43,10,42,18,21,17,39,15,20,25,6,108,22,7,23]
INCOME_CATEGORY_ID = [92,29,30,96,32,225,27,114,227]
TRANSFERS = [28,36,40,26]

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

def getTransactions(accountId,from_year='1900',from_month='01',from_day='01',to_year='2020',to_month='01',to_day='01',container='bank'):
    data = {
        "container": container,
        "accountId": accountId,
        "fromDate": from_year +"-"+ from_month +"-"+ from_day,
        "toDate": to_year +"-"+ to_month +"-"+ to_day
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions", headers=INFO['headers'], params=data)
    return req.json()

def getAccount(accountId):
    accounts = getAccounts()
    for acc in accounts:
        if str(acc['id']) == str(accountId):
            return acc
    return None

def getTotalExpenses(accountId, from_year=1900, from_month=1, from_day=1, to_year=2020, to_month=1, to_day=1):
    data = {
        'accountId': accountId,
    	'categoryId': ','.join([str(x) for x in EXPENSES_CATEGORY_ID]),
    	'groupBy':'CATEGORY',
    	"fromDate": "%s-%s-%s" % (from_year, from_month, from_day),
        "toDate": "%s-%s-%s" % (to_year, to_month, to_day),
    	'categoryType': 'EXPENSE',
    	'interval': 'M',
    	'include': 'details'
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/derived/transactionSummary",headers= INFO['headers'],params = data)
    try:
        expense = req.json()["transactionSummary"][0]['debitTotal']['amount']
        return expense
    except:
        return 0

def getTransactionsSummary(account,from_year,to_year,from_month,to_month,from_day,to_day,category_id,category_type):
    data = {
        'accountId': account,
    	'categoryId': str(category_id),
    	'groupBy':'CATEGORY',
    	"fromDate": from_year + "-" + from_month + "-" + from_day,
        "toDate": to_year + "-" + to_month + "-" + to_day,
    	'categoryType': category_type,
    	'interval': 'M',
    	'include': 'details'
        }
    req = requests.get("https://developer.api.yodlee.com/ysl/derived/transactionSummary",headers= INFO['headers'],params = data)
    return req.json()

def getExpensesByCategory(accountId, from_year='1900', from_month='01', from_day='01', to_year='2020', to_month='01', to_day='01'):
    result = []
    for i in EXPENSES_CATEGORY_ID:
            try:
                sample_json_take_2 = getTransactionsSummary(accountId,from_year,to_year,from_month,to_month,from_day,to_day,i,"EXPENSE")
                expense = sample_json_take_2["transactionSummary"][0]['debitTotal']['amount']
                if (expense > 0):
                    if(i == 3):
                        result.append("Charitable Giving: " + str(expense))
                    elif(i == 9):
                        result.append("Gifts: " + str(expense))
                    elif(i == 2):
                        result.append("Automative/Fuel: " + str(expense))
                    elif(i == 11):
                        result.append("Healthcare/Medical: " +  str(expense))
                    elif(i == 14):
                        result.append("insurance: " + str(expense))
                    elif(i == 45):
                        result.append("Office expenses: " + str(expense))
                    elif(i == 16):
                        result.append("Services/Supplies: " + str(expense))
                    elif(i == 104):
                        result.append("Postage/Shipping: " + str(expense))
                    elif(i == 37):
                        result.append("Taxes: " + str(expense))
                    elif(i == 19):
                        result.append("Other Expenses: " + str(expense))
                    elif(i == 33):
                        result.append("Check/Payment: " + str(expense))
                    elif(i == 24):
                        result.append("Service Charges/ Fees: " + str(expense))
                    elif(i == 13):
                        result.append("Home Improvement: " + str(expense))
                    elif(i == 43):
                        result.append("Electrics/General Merchandise: " + str(expense))
                    elif(i == 10):
                        result.append("Groceries: " + str(expense))
                    elif(i == 42):
                        result.append("Pets/Pet Care: " + str(expense))
                    elif(i == 18):
                        result.append("Mortgage: " + str(expense))
                    #----------------------------------------
                    elif(i == 21):
                        result.append("Rent: " + str(expense))
                    elif(i == 17):
                        result.append("Loans: " + str(expense))
                    elif(i == 39):
                        result.append("Utilities: " + str(expense))
                    elif(i == 15):
                        result.append("Cable: " + str(expense))
                    elif(i == 20):
                        result.append("Personal/Family: " + str(expense))
                    elif(i == 25):
                        result.append("ATM/Cash Withdraws: " + str(expense))
                    elif(i == 6):
                        result.append("Education: " + str(expense))
                    elif(i == 108):
                        result.append("Subscription Renewals: " + str(expense))
                    elif(i == 22):
                        result.append("Restaurants: " + str(expense))
                    elif(i == 7):
                        result.append("Entertainment/Recreation: " + str(expense))
                    elif(i == 23):
                        result.append("Travel: " + str(expense))
                #print("User: " + str(user) + "Account" + str(j) + "Sum of expenses: " + str(sum_of_expenses))
            except:
                pass
    return result

def getTotalIncome(accountId, from_year=1900, from_month=1, from_day=1, to_year=2020, to_month=1, to_day=1):
    data = {
        'accountId': accountId,
    	'categoryId': ','.join([str(x) for x in INCOME_CATEGORY_ID]),
    	'groupBy':'CATEGORY',
    	"fromDate": "%s-%s-%s" % (from_year, from_month, from_day),
        "toDate": "%s-%s-%s" % (to_year, to_month, to_day),
    	'categoryType': 'INCOME',
    	'interval': 'M',
    	'include': 'details'
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/derived/transactionSummary",headers= INFO['headers'],params = data)
    try:
        income = req.json()["transactionSummary"][0]['creditTotal']['amount']
        return income
    except:
        return 0

def getIncomeByCategory(accountId, from_year='1900', from_month='01', from_day='01', to_year='2020', to_month='01', to_day='01'):
    result = []
    for i in INCOME_CATEGORY_ID:
        try:
            #print("transaction summary: " + getTransactionsSummary(accounts[0],'1900','2020','01','12','01','28',i))
            sample_json_take_3 = getTransactionsSummary(accountId,from_year,to_year,from_month,to_month,from_day,to_day,i,"INCOME")
            income = sample_json_take_3["transactionSummary"][0]['creditTotal']['amount']
            if (income > 0):
                if(i == 92):
                    result.append("Sales/Service Income: " + str(income))
                elif(i == 29):
                    result.append("Salary/Regular  Income: " + str(income))
                elif(i == 30):
                    result.append("Investment/Retirement Income: " + str(income))
                elif(i == 96):
                    result.append("Interest Income: " +  str(income))
                elif(i == 32):
                    result.append("Other Income: " + str(income))
                elif(i == 225):
                    result.append("Rewards: " + str(income))
                elif(i == 27):
                    result.append("Deposits: " + str(income))
                elif(i == 114):
                    result.append("Expenses Reimbursements: " + str(income))
                elif(i == 227):
                    result.append("Refunds/Adjustments: " + str(income))
        except:
            pass
    return result

def getTransactionsCount(account,from_year=1900, from_month=1, from_day=1, to_year=2020, to_month=1, to_day=1, container_input='bank'):
    data = {
        "container": container_input,
        "accountId": account,
        "fromDate": "%s-%s-%s" % (from_year, from_month, from_day),
        "toDate": "%s-%s-%s" % (to_year, to_month, to_day)
    }

    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/count",headers= INFO['headers'],params = data)
    return req.json()

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
