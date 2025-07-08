from flask import Blueprint,render_template,request,redirect
from flask_login import login_user
from models.user import *
from passlib.hash import sha256_crypt
from extensions import db

app = Blueprint('users',__name__)

#user login page address
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("users/login.html")
    else:
        register = request.form.get("register",None)
        username = request.form.get("username")
        password = request.form.get("password")
        phone = request.form.get("phone")
        address = request.form.get("address")
        if register != None:
            user = User(
                username = username,
                password = sha256_crypt.encrypt(password),
                phone = phone,
                address = address
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect("/users/dashboard")
