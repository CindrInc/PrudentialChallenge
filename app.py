from flask import Flask, render_template, request, redirect, url_for
import yodlee_attempt

app = Flask("Prudential Challenge")

yodlee_attempt.init(yodlee_attempt.INFO['users'][0])

# def checkError()

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = yodlee_attempt.init({
            "loginName": request.form['username'],
            "password": request.form['password'],
            "locale": 'en_US'
        })
        if result:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route("/home")
def home():
    accounts = yodlee_attempt.getAccounts()
    return render_template('home.html', accounts=accounts)

@app.route("/transactions/<accountId>/<id>")
def transactionDetails(accountId, id):
    print(accountId, id)
    transactions = yodlee_attempt.getAllTransactions(accountId)['transaction']
    tran = None
    for t in transactions:
        if str(t['id']) == str(id):
            tran = t
            break
    return render_template('transaction_details.html', account=accountId, tran=tran)

@app.route("/transactions/<accountId>")
def transactions(accountId):
    transactions = yodlee_attempt.getAllTransactions(accountId)['transaction']
    return render_template('transactions.html', account=accountId, tran=transactions)

