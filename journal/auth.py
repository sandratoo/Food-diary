from xmlrpc.client import boolean
from flask import Blueprint,render_template,request,flash

auth = Blueprint("auth",__name__)

@auth.route("/")
def index():
    return render_template("index.html")

@auth.route("/login", methods=["POST","GET"])
def login():
    data = request.form
    print(data)
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

        if len(username) < 3:
            flash("Username must be atleast 3 characters!", category="error")
        elif len(email) < 6:
             flash("Email must be atleast 6 characters!", category="error")
        elif password1 != password2:
            flash("Passwords do not match!", category="error")
        else:
            flash("Account has been created!", category="success")
            return render_template("login.html")


    return render_template("signup.html")