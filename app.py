from flask import Flask, render_template
import yodlee_attempt

yodlee_attempt.init()

app = Flask("Prudential Challenge")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/accounts")
def accounts():
    accounts = yodlee_attempt.getAccounts()
    return render_template('accounts.html', accounts=accounts)

@app.route("/transactions/<accountId>")
@app.route("/transactions/<accountId>/<id>")
def transactions(accountId, id=None):
    transactions = yodlee_attempt.getTransactions(accountId)['transaction']
    if id is None:
        # print(transactions)
        return render_template('transactions.html', account=accountId, tran=transactions)
    else:
        result = None
        for tran in transactions:
            if str(tran['id']) == id:
                result = tran
                print(result)
        return render_template('transactions.html', account=accountId, tran=result)
