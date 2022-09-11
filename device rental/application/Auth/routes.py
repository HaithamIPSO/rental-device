from flask import Blueprint,redirect,flash,render_template,request,url_for
from application.Auth.forms import LoginForm,RegisterationForm
from application.models import Users
from werkzeug.security import generate_password_hash,check_password_hash
import os
from sqlalchemy import text
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
from application import db
auth  = Blueprint('auth', __name__,template_folder='templates',static_folder='../static')

@auth.route("/login",methods=["POST","GET"])
def Login():
    if current_user.is_authenticated:
        flash("You need to be logged out to be able to login")
        return '<script>window.history.back()</script>'
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        
        user = Users.query.filter_by(email=form.email.data).first()
       
        if user and check_password_hash(user.password,form.password.data):
            if user.is_admin == 1:
                login_user(user, True)
                return redirect(url_for('admin.Index'))
            else:
                login_user(user,True)
                return redirect(url_for('main.Index'))
        else:
            flash("Login Unsuccessful. Please check email and password")

    return render_template('auth/login.html',form=form)




@auth.route("/register", methods=["POST","GET"])
def Register():
    if current_user.is_authenticated:
        flash("You need to be loggedout to be able to register")
        return '<script>window.history.back()</script>'

    form = RegisterationForm()
    if request.method == 'POST' and form.validate():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            flash("Email Already Exist.Please Try Another One")
        else:
            user = Users(email=form.email.data,password=generate_password_hash(form.password.data),firstname=form.firstname.data,lastname=form.lastname.data,age=form.age.data,phone_number=form.phone.data,gender=form.gender.data,is_admin=0)
            db.session.add(user)
            db.session.commit()
            flash("Registered Successfully")
            return redirect(url_for("auth.Login"))
    return render_template('auth/register.html',form=form)