import os

from cs50 import SQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, case
from sqlalchemy.sql.expression import literal
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


from helpers import apology, login_required, lookup, usd, validate_password

# Configure application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:/Users/Mohamed/Desktop/COMPUTER SCIENCE/cs50/CS50x/week-9-flask/finance/finance.db'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash = db.Column(db.String(120), nullable=False)
    cash = db.Column(db.Float, default=10000.00, nullable=False)


# define the Purchase model
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # define a relationship between Purchase and User models
    user = db.relationship('Users', backref=db.backref('purchases', lazy=True))

    __tablename__ = "purchases"  # Updated table name

    def __repr__(self):
        return f"Purchase(user_id={self.user_id}, symbol='{self.symbol}', shares={self.shares}, price={self.price}, timestamp={self.timestamp})"


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # get user's portfolio from the database
    user_id = session["user_id"]
    portfolio = db.session.query(Purchase.symbol,
                                 func.sum(Purchase.shares),
                                 func.avg(Purchase.price)).\
        filter_by(user_id=user_id).\
        group_by(Purchase.symbol).\
        having(func.sum(Purchase.shares) > 0).\
        all()

    # lookup current prices for each stock
    stocks = []
    total_value = 0
    for stock in portfolio:
        quote = lookup(stock[0])
        value = quote["price"] * stock[1]
        stocks.append({
            "symbol": stock[0],
            "name": quote["name"],
            "shares": stock[1],
            "price": usd(quote["price"]),
            "total": usd(value)
        })
        total_value += value

    # get user's current cash balance
    user = Users.query.get(user_id)
    cash = user.cash

    # calculate grand total
    grand_total = cash + total_value

    return render_template("index.html", stocks=stocks, cash=usd(cash), total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        # Ensure a symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)
        # Ensure the quote does exist
        elif not quote:
            return apology("Invalid symbol")

        # Ensure number of shares was submitted
        elif not request.form.get("shares"):
            return apology("must provide number of shares", 403)

        elif not int(request.form.get("shares")) or int(request.form.get("shares")) <= 0:
            return apology("must provide number of shares", 403)

            # Check if user has enough cash to buy the stock
        shares = int(request.form.get("shares"))
        user_id = session["user_id"]
        user = Users.query.filter_by(id=user_id).first()
        if user.cash < quote["price"] * shares:
            return apology("not enough cash", 400)

        # Update user's cash balance
        user.cash -= quote["price"] * shares
        db.session.commit()

        # Insert purchase into database
        purchase = Purchase(user_id=user.id, symbol=symbol.upper(),
                            shares=shares, price=quote["price"])

        # add the new purchase to the session and commit the transaction
        db.session.add(purchase)
        db.session.commit()

        return redirect("/")

    if request.method == "GET":
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # get user id and all purchases and sales made by the user
    user_id = session["user_id"]

    transactions = db.session.query(
        Purchase.symbol, Purchase.shares, Purchase.price, Purchase.timestamp,
        case([(Purchase.shares < 0, func.abs(Purchase.shares))],
             else_=Purchase.shares),
        case([(Purchase.shares < 0, "Sell")], else_="Buy")
    ).filter_by(user_id=user_id).order_by(Purchase.timestamp.asc()).all()

    # get the name of each stock and add it to transactions
    # get the name of each stock and add it to transactions
    for i, transaction in enumerate(transactions):
        symbol = transaction[0]
        name = lookup(symbol)["name"]
        transactions[i] = tuple(transaction)  # convert Row to tuple
        # add stock name to transaction tuple
        transactions[i] = (name,) + transactions[i]

    # render transactions as a HTML table
    return render_template("history.html", transactions=transactions)


@ app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        user = Users.query.filter_by(
            username=request.form.get("username")).first()

        # Ensure username exists and password is correct
        if not user or not check_password_hash(user.hash, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user.id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@ app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@ app.route("/quote", methods=["GET", "POST"])
@ login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if quote:
            return render_template("quoted.html", quote=quote)
        else:
            return apology("Invalid symbol")
    else:
        return render_template("quote.html")


@ app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
# User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Validate the password
        elif not validate_password(request.form.get("password")):
            return apology("Password must contain at least one letter, one number, and one symbol", 400)

            # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

         # Ensure username does not exist
        # Query database for registered usernames
        user = Users.query.filter_by(
            username=request.form.get("username")).first()

        if user is not None:
            return apology("username already exists", 409)

        else:
            new_user = Users(username=request.form.get("username"),
                             hash=generate_password_hash(request.form.get("password")))
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! You can now log in.", "success")
            return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # get user id and symbols of stocks owned by the user
    user_id = session["user_id"]
    owned_stocks = db.session.query(
        Purchase.symbol, func.sum(Purchase.shares)
    ).filter_by(user_id=user_id).group_by(Purchase.symbol).all()

    # create a list of tuples with owned stocks and their total shares
    owned_stocks = [(symbol, shares) for symbol, shares in owned_stocks]

    # if the form was submitted
    if request.method == "POST":

        # ensure a stock symbol was submitted
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide stock symbol", 400)

        # ensure the user owns shares of the stock
        shares_owned = None
        for owned_symbol, owned_shares in owned_stocks:
            if owned_symbol == symbol:
                shares_owned = owned_shares
                break

        if shares_owned is None or shares_owned <= 0:
            return apology("you do not own any shares of this stock", 400)

        # ensure a number of shares was submitted
        shares = request.form.get("shares")
        if not shares:
            return apology("must provide number of shares", 400)

        # ensure the input is a positive integer
        try:
            shares = int(shares)
        except ValueError:
            return apology("number of shares must be a positive integer", 400)

        if shares <= 0:
            return apology("number of shares must be a positive integer", 400)

        if shares > shares_owned:
            return apology("you do not own that many shares of this stock", 400)

        # get the current price of the stock
        quote = lookup(symbol)

        # calculate the total sale value
        total_sale = shares * quote["price"]

        # update user's cash balance
        user = Users.query.get(user_id)
        user.cash += total_sale

        # insert sale record into purchases table
        sale = Purchase(user_id=user_id, symbol=symbol.upper(),
                        shares=-shares, price=quote["price"])
        db.session.add(sale)
        db.session.commit()

        # redirect user to home page
        return redirect("/")

    # if the request method is GET, render the sell form
    else:
        return render_template("sell.html", stocks=owned_stocks)


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow users to change their passwords"""

    # get user id
    user_id = session["user_id"]

    if request.method == "POST":
        # get old password and new password from form
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        if not request.form.get("old_password"):
            return apology("must provide your old password", 400)

        if not request.form.get("new_password"):
            return apology("must provide your new password", 400)

        if not request.form.get("confirm_new_password"):
            return apology("must provide password confirmation", 400)

        elif not validate_password(request.form.get("new_password")):
            return apology("Password must contain at least one letter, one number, and one symbol")

        # Ensure passwords match
        if request.form.get("new_password") != request.form.get("confirm_new_password"):
            return apology("passwords must match", 400)

        # get user from database
        user = Users.query.get(user_id)

        # check if old password is correct
        if not check_password_hash(user.hash, old_password):
            flash("Old password is incorrect")
            return redirect("/change_password")

        # hash and store new password
        user.hash = generate_password_hash(new_password)
        db.session.commit()

        flash("Password changed successfully")
        return redirect("/")

    # render change password form
    return render_template("change_password.html")


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Allow users to add additional cash to their account"""

    # get user id
    user_id = session["user_id"]

    if request.method == "POST":
        # get amount of cash to add from form
        cash = float(request.form.get("cash"))

        # add cash to user's balance in database
        user = Users.query.get(user_id)
        user.cash += cash
        db.session.commit()

        flash("Cash added successfully")
        return redirect("/")

    # render add cash form
    return render_template("add_cash.html")
