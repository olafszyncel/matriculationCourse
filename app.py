import os
import stripe

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51KoB0wDzQaz1vRvqMoil5RLqwvB8fjq1nBoztq5SJzt8ORCKPs96X4Nu5IqK0fttQtTKavnCwaXjbl9RuRd0XQMa007MDh20TN'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51KoB0wDzQaz1vRvqWSZdYiaVDUri3FiBckbA7ymvXsl6Tvsjsi73ivdVSsHNbAexFUAVvvvO0Auc8cam90QOEpCB007a6r0Wyi'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    # Display the entries in the database on index.html
    render_template("index.html")

    return render_template("index.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    render_template("buy.html")

    if request.method == "POST":

        a = request.form.get("adv")
        print(a)
        b = request.form.get("bas")
        email = b
        cash = db.execute("SELECT cash FROM users WHERE id = ?", email)


        return courses()

    """Buy shares of stock"""

    return render_template("buy.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure email was submitted
        if not request.form.get("email"):
            flash("Must provide email!")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password!")
            return render_template("login.html")

        # Query database for email
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Invalid email or/and passwoord!")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        flash("You are successfuly logged in!")

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


@app.route("/forms", methods=["GET", "POST"])
@login_required
def forms():

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1KoBNHDzQaz1vRvqTT0TRYCw',
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=url_for('index', _external=True),
    )
    return render_template("forms.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "POST":

        # check the fill of input
        if not request.form.get("email"):
            flash("Must provide email!")
            return render_template("register.html")

        elif not request.form.get("name"):
            flash("Must provide name!")
            return render_template("register.html")

        elif not request.form.get("password"):
            flash("Must provide password!")
            return render_template("register.html")

        elif not request.form.get("confirmation"):
            flash("Must provide password again!")
            return render_template("register.html")

        elif request.form.get("password") != request.form.get("confirmation"):
            flash("Passwords must be the same!")
            return render_template("register.html")

        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))
        if len(rows) != 0:
            flash("This email is already exist!")
            return render_template("register.html")

        # Add user to database
        db.execute("INSERT INTO users (email, name, hash) VALUES(?, ?, ?)", request.form.get("email"), request.form.get("name"), generate_password_hash(request.form.get("password")))

        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        flash("You are successfuly signed up!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/courses", methods=["GET", "POST"])
@login_required
def courses():
    # sprawdza w bazie jakie ma kursy uzytkownik i je wypisuje
    return render_template("courses.html")

# Basic course
@app.route("/courses/bas", methods=["GET", "POST"])
@login_required
def bas():
    # jesli uzytkownik nie posiada kursu o tej nazwie funkcja zwraca buy.html i napis ze nie ma tego kursu
    return render_template("basic.html")

# Advanced course
@app.route("/courses/adv", methods=["GET", "POST"])
@login_required
def adv():

    # jesli uzytkownik nie posiada kursu o tej nazwie funkcja zwraca buy.html i napis ze nie ma tego kursu
    return render_template("advanced.html")

if __name__=="__main__":
    app.run(debug=True)