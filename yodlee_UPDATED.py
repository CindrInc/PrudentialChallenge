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

def printTransactionCategories(account,from_year,to_year,from_month,to_month,from_day,to_day):
    data = {
        "container": "creditCard",
        "accountId": account['id'],
        "fromDate": from_year + "-" + from_month + "-" + from_day,
        "toDate": to_year + "-" + to_month + "-" + to_day
    }
    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/categories", headers=INFO['headers'],params =data)
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
def getTransactionsCount(account,from_year,to_year,from_month,to_month,from_day,to_day,container_input):
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
        "container": container_input,
        "accountId": account['id'],
        "fromDate": from_year + "-" + from_month + "-" + from_day,
        "toDate": to_year + "-" + to_month + "-" + to_day
    }

    req = requests.get("https://developer.api.yodlee.com/ysl/transactions/count",headers= INFO['headers'],params = data)
    return req.json()
def getTransactionsSummary(account,from_year,to_year,from_month,to_month,from_day,to_day,category_id,category_type):
    data = {
        'accountId': account['id'],
    	'categoryId': str(category_id),
    	'groupBy':'CATEGORY',
    	"fromDate": from_year + "-" + from_month + "-" + from_day,
        "toDate": to_year + "-" + to_month + "-" + to_day,
    	'categoryType': category_type,
    	'interval': 'M',
    	'include': 'details'
        }
    req = requests.get("https://developer.api.yodlee.com/ysl/derived/transactionSummary",headers= INFO['headers'],params = data)
    return json.dumps(req.json(), indent=4)

EXPENSES_CATEGORY_ID = [3,9,2,11,14,45,16,104,37,19,33,24,13,43,10,42,18,21,17,39,15,20,25,6,108,22,7,23]
INCOME_CATEGORY_ID = [92,29,30,96,32,225,27,114,227]
TRANSFERS = [28,36,40,26]
print(len(EXPENSES_CATEGORY_ID))




getCobrandToken()

'''sample_json = {}
sample_json_take_2 = json.loads(getTransactionsSummary(accounts[0],'1900','2020','01','12','01','28',2))
print(sample_json_take_2["transactionSummary"][0]['debitTotal']['amount']) #gives total amount
expense = sample_json_take_2["transactionSummary"][0]['debitTotal']['amount']
sum_of_expenses = 0
print(sum_of_expenses + expense)'''
j = 0
user_index = 0
for user in INFO['users']:
    getUserToken(user)
    accounts = getAccounts()
    for account in accounts:
        print(" Now calculating your expenses")
        sum_of_expenses = 0
        for i in EXPENSES_CATEGORY_ID:
            try:
                #print("id: " + str(i))
                expense = 0
                #print("transaction summary: " + getTransactionsSummary(accounts[0],'1900','2020','01','12','01','28',i))
                sample_json_take_2 = json.loads(getTransactionsSummary(account,'1900','2020','01','12','01','28',i,"EXPENSE"))
                expense = sample_json_take_2["transactionSummary"][0]['debitTotal']['amount']
                if (expense > 0):
                    if(i == 3):
                        print("Charitable Giving: " + str(expense))
                    elif(i == 9):
                        print("Gifts: " + str(expense))
                    elif(i == 2):
                        print("Automative/Fuel: " + str(expense))
                    elif(i == 11):
                        print("Healthcare/Medical: " +  str(expense))
                    elif(i == 14):
                        print("insurance: " + str(expense))
                    elif(i == 45):
                        print("Office expenses: " + str(expense))
                    elif(i == 16):
                        print("Services/Supplies: " + str(expense))
                    elif(i == 104):
                        print("Postage/Shipping: " + str(expense))
                    elif(i == 37):
                        print("Taxes: " + str(expense))
                    elif(i == 19):
                        print("Other Expenses: " + str(expense))
                    elif(i == 33):
                        print("Check/Payment: " + str(expense))
                    elif(i == 24):
                        print("Service Charges/ Fees: " + str(expense))
                    elif(i == 13):
                        print("Home Improvement: " + str(expense))
                    elif(i == 43):
                        print("Electrics/General Merchandise: " + str(expense))
                    elif(i == 10):
                        print("Groceries: " + str(expense))
                    elif(i == 42):
                        print("Pets/Pet Care: " + str(expense))
                    elif(i == 18):
                        print("Mortgage: " + str(expense))
                    #----------------------------------------
                    elif(i == 21):
                        print("Rent: " + str(expense))
                    elif(i == 17):
                        print("Loans: " + str(expense))
                    elif(i == 39):
                        print("Utilities: " + str(expense))
                    elif(i == 15):
                        print("Cable: " + str(expense))
                    elif(i == 20):
                        print("Personal/Family: " + str(expense))
                    elif(i == 25):
                        print("ATM/Cash Withdraws: " + str(expense))
                    elif(i == 6):
                        print("Education: " + str(expense))
                    elif(i == 108):
                        print("Subscription Renewals: " + str(expense))
                    elif(i == 22):
                        print("Restaurants: " + str(expense))
                    elif(i == 7):
                        print("Entertainment/Recreation: " + str(expense))
                    elif(i == 23):
                        print("Travel: " + str(expense))
                sum_of_expenses += expense
                #print("User: " + str(user) + "Account" + str(j) + "Sum of expenses: " + str(sum_of_expenses))
            except:
                pass #this is because some of the categories there are no expenses so the json is empty
        print("User: " + str(user_index) + " Account" + str(j) + " Sum of expenses: " + str(sum_of_expenses))
        print(" Now calculating your incomes")
        sum_of_incomes = 0
        for i in INCOME_CATEGORY_ID:
                try:
                    #print("id: " + str(i))
                    income = 0
                    #print("transaction summary: " + getTransactionsSummary(accounts[0],'1900','2020','01','12','01','28',i))
                    sample_json_take_3 = json.loads(getTransactionsSummary(account,'1900','2020','01','12','01','28',i,"INCOME"))
                    income = sample_json_take_3["transactionSummary"][0]['creditTotal']['amount']
                    if (income > 0):
                        if(i == 92):
                            print("Sales/Service Income: " + str(income))
                        elif(i == 29):
                            print("Salary/Regular  Income: " + str(income))
                        elif(i == 30):
                            print("Investment/Retirement Income: " + str(income))
                        elif(i == 96):
                            print("Interest Income: " +  str(income))
                        elif(i == 32):
                            print("Other Income: " + str(income))
                        elif(i == 225):
                            print("Rewards: " + str(income))
                        elif(i == 27):
                            print("Deposits: " + str(income))
                        elif(i == 114):
                            print("Expenses Reimbursements: " + str(income))
                        elif(i == 227):
                            print("Refunds/Adjustments: " + str(income))
                    sum_of_incomes += income
                except:
                    pass #this is because some of the categories there are no incomes so the json is empty
        print("User: " + str(user_index) + " Account" + str(j) + " Sum of incomes: " + str(sum_of_incomes))
        print("User: " + str(user_index) + " Account " + str(j)+" Number of transactions for credit card: ",getTransactionsCount(account,'1900','2020','01','12','01','28','creditCard'))
        print("User: " + str(user_index) + " Account " + str(j)+" Number of transactions for bank: ",getTransactionsCount(account,'1900','2020','01','12','01','28','bank'))
        print("User: " + str(user_index) + " Account " + str(j)+" Number of transactions for investment: ",getTransactionsCount(account,'1900','2020','01','12','01','28','investment'))
        print("User: " + str(user_index) + " Account " + str(j)+" Number of transactions for insurance: ",getTransactionsCount(account,'1900','2020','01','12','01','28','insurance'))
        print("User: " + str(user_index) + " Account " + str(j)+" Number of transactions for loan: ",getTransactionsCount(account,'1900','2020','01','12','01','28','loan'))
        j += 1 #this is just to keep track of accounts'''
        user_index += 1


'''for account in accounts:
        #account,from_year,to_year,from_month,to_month,from_day,to_day)
        printTransactionCategories(account,'1900','2020','01','12','01','28')
        print("Number of transactions: ",getTransactionsCount(account,'1900','2020','01','12','01','28'))
        print("transaction summary: ",getTransactionsSummary(account,'1900','2020','01','12','01','28'))
        #print("Transactions: ",getTransactions(account,'1900','2020','01','12','01','28'))
        break
        '''
'''for i in range(len(INFO['users'])):
    getUserToken(INFO['users'][i])
    accounts = getAccounts()
    for account in accounts:
        print("Number of transactions: ",getTransactionsCount(account))
        print("Transactions: ",getTransactions(account))'''
