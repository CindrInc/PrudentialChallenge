from flask import Flask, render_template, request, redirect, url_for
import yodlee_attempt1 as yodlee_attempt

app = Flask("Prudential Challenge")

yodlee_attempt.init(yodlee_attempt.INFO['users'][0])

# def checkError()
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

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
    transactions = yodlee_attempt.getTransactions(accountId)['transaction']
    tran = None
    for t in transactions:
        if str(t['id']) == str(id):
            tran = t
            break
    return render_template('transaction_details.html', account=accountId, tran=tran)

@app.route("/viewAccount/<accountId>")
def viewAccount(accountId):
    args = request.args
    account = yodlee_attempt.getAccountById(accountId)
    transactions = yodlee_attempt.getTransactions(accountId, args['from_year'], args['from_month'], args['from_day'], args['to_year'], args['to_month'], args['to_day'])
    if 'transaction' in transactions:
        transactions = transactions['transaction']
    totalExpense = yodlee_attempt.getTotalExpenses(accountId, args['from_year'], args['from_month'], args['from_day'], args['to_year'], args['to_month'], args['to_day'])
    totalIncome = yodlee_attempt.getTotalIncome(accountId, args['from_year'], args['from_month'], args['from_day'], args['to_year'], args['to_month'], args['to_day'])
    expenseCategoryBreakdown = yodlee_attempt.getExpensesByCategory(accountId, args['from_year'], args['from_month'], args['from_day'], args['to_year'], args['to_month'], args['to_day'])
    incomeCategoryBreakdown = yodlee_attempt.getIncomeByCategory(accountId, args['from_year'], args['from_month'], args['from_day'], args['to_year'], args['to_month'], args['to_day'])
    print(transactions, totalExpense, totalIncome, expenseCategoryBreakdown, incomeCategoryBreakdown)
    return render_template('viewAccount.html', account=account, tran=transactions if len(transactions) is not 0 else 0, totalExpense=totalExpense, totalIncome=totalIncome, expenseCategoryBreakdown=expenseCategoryBreakdown, incomeCategoryBreakdown=incomeCategoryBreakdown)
