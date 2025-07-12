from flask import Blueprint,render_template,request,redirect,flash,url_for
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
        phone = request.form.get("phone",None)
        address = request.form.get("address",None)
        if register != None:
            user = User.query.filter(User.username == username).first()
            if user != None:
                flash("این نام کاربری قبلا ثبت شده است")
                return redirect(url_for("users.login"))
            
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

        else:
            user = User.query.filter(User.username == username).first()
            if user == None:
                flash("نام کاربری یا رمز عبور اشتباه است")
                return redirect(url_for("users.login"))

            if sha256_crypt.verify(password, user.password):
                login_user(user)
                return redirect("/users/dashboard")
            else:
                flash("نام کاربری یا رمز عبور اشتباه است")
                return redirect(url_for("users.login"))