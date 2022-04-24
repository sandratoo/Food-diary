from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth",__name__)

@auth.route("/")
def index():
    return render_template("index.html")

@auth.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Successfully logged in!")
                return redirect(url_for("auth.index"))
            else:
                flash("Wrong password!")
        flash("Email does not exist!")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<h1>Logout</h1>"

@auth.route("/signup", methods=["POST","GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email= request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists!")

        elif len(username) < 3:
            flash("Username must be atleast 3 characters!", category="error")
        elif len(email) < 6:
             flash("Email must be atleast 6 characters!", category="error")
        elif password1 != password2:
            flash("Passwords do not match!", category="error")
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account has been created!", category="success")
            return redirect(url_for("auth.login"))


    return render_template("signup.html")