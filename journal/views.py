from flask import Blueprint, render_template,request,redirect,url_for,flash
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/index", methods=["POST","GET"])
@login_required
def index():
    if request.method == "POST":
        note = request.form.get("note")

        new_note = Note(data=note, user_id= current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash("Food log added to sucessfully!")
    return render_template("index.html",user=current_user)

@views.route("/delete", methods=["POST","GET"])
def delete():
    delete_note = Note.query.filter_by(id=Note.id).first()
    db.session.delete(delete_note)
    db.session.commit()
    return redirect(url_for("views.index"))
