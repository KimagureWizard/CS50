import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    user_id = session["user_id"]
    overview_dict = db.execute("SELECT symbol, shares, buy_price, sell_price FROM inventory WHERE user_id = ?", user_id)
    new_overview_dict = {}

    for item in overview_dict:
        symbol = item["symbol"]
        shares = item["shares"]
        stock_info = lookup(symbol)
        current_price = stock_info["price"]
        if item["sell_price"] != None:
            shares = -shares
        if symbol in new_overview_dict:
            new_overview_dict[symbol]["shares"] += shares
        else:
            new_overview_dict[symbol] = {"shares": shares, "current_price": current_price}

    return render_template("index.html", new_overview_dict=new_overview_dict)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]
        stock = request.form.get("stock_code")
        stock_info = lookup(stock)
        symbol = stock_info["name"]
        price = stock_info["price"]
        share = int(request.form.get("stock_shares"))
        time = datetime.datetime.now()
        fund_dict = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        fund = fund_dict[0]["cash"]
        cost = float(price * share)

        if stock_info == None:
            return apology("Stock Not Found")
        elif cost > fund:
            return apology("Not enough balance")
        else:
            fund -= cost
            fund = "{:.2f}".format(fund)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", float(fund), user_id)
            db.execute("INSERT INTO inventory (user_id, symbol, shares, buy_price, buy_time) VALUES (?, ?, ?, ?, ?)", user_id, symbol, share, price, time)
        return redirect("/buy")

    return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    buy_overview_dict = db.execute("SELECT symbol, shares, buy_price, buy_time FROM inventory WHERE user_id = ? AND sell_price IS NULL", user_id)
    sell_overview_dict = db.execute("SELECT symbol, shares, sell_price, sell_time FROM inventory WHERE user_id = ? AND buy_price IS NULL", user_id)

    return render_template("history.html", buy_overview_dict=buy_overview_dict, sell_overview_dict=sell_overview_dict)


@app.route("/login", methods=["GET", "POST"])
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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    name = None
    price = None
    display_value = "none"

    if request.method == "POST":
        stock = request.form.get("stock_code")
        stock_info = lookup(stock)
        if stock_info == None:
            return apology("Stock Not Found")

        name = stock_info["name"]
        price = stock_info["price"]
        display_value = "block"

    return render_template("quote.html", search_name=name, search_price=price, display_value=display_value)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        register_time = datetime.datetime.now()
        db.execute("INSERT INTO users (username, hash, registration_time) VALUES (?, ?, ?)", username, generate_password_hash(password), register_time)

        return redirect("/login")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]
        stock = request.form.get("stock_code")
        stock_info = lookup(stock)
        symbol = stock_info["name"]
        sell_time = datetime.datetime.now()
        owned_stock_dict = db.execute("SELECT symbol FROM inventory WHERE user_id = ?", user_id)
        stock_found = False
        sell_price = stock_info["price"]
        share = int(request.form.get("stock_shares"))
        fund_dict = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        fund = float(fund_dict[0]["cash"])
        profit = float(sell_price * share)

        if stock_info == None:
            return apology("Stock Not Found")
        for items in owned_stock_dict:
            if (symbol == items["symbol"]):
                stock_found = True
                owned_share_dict = db.execute("SELECT shares FROM inventory WHERE symbol = ? AND sell_time IS NULL", symbol)
                owned_share = 0
                for shares in owned_share_dict:
                    sell_price = stock_info["price"]
                    share = int(request.form.get("stock_shares"))
                    fund_dict = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
                    fund = float(fund_dict[0]["cash"])
                    profit = float(sell_price * share)
                    owned_share += shares["shares"]
                if share > owned_share:
                    return apology("Not enough share to sell")
        if not stock_found:
            return apology("Stock Not Found")

        fund += profit
        fund = "{:.2f}".format(fund)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", fund, user_id)
        db.execute("INSERT INTO inventory (user_id, symbol, shares, sell_price, sell_time) VALUES (?, ?, ?, ?, ?)", user_id, symbol, share, sell_price, sell_time)
        return redirect("/sell")

    return render_template("sell.html")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    """Manage user profile"""
    if request.method == "POST":
        user_id = session["user_id"]
        fund_dict = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        fund = fund_dict[0]["cash"]
        topup = int(request.form.get("topup"))
        fund += topup
        db.execute("UPDATE users SET cash = ? WHERE id = ?", fund, user_id)
        return redirect("/profile")

    user_id = session["user_id"]
    name_dict = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    name = name_dict[0]["username"]
    time_dict = db.execute("SELECT registration_time FROM users WHERE id = ?", user_id)
    time = time_dict[0]["registration_time"]
    fund_dict = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    fund = fund_dict[0]["cash"]
    return render_template("profile.html", register_time=time, money=fund, name=name)



@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change password"""
    if request.method == "POST":

        user_id = session["user_id"]

        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("wrong password", 403)

        else:
            new_password = request.form.get("new_password")
            db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(new_password), user_id)

        return redirect("/")

    else:
        return render_template("change_password.html")
