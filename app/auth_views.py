from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

import re

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    regmail = re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")
    regpassword = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$")
    
    if(regmail.match(email) == None):
        flash('Error in Email.', 'warning')
        return redirect(url_for('auth.login'))
   
    if(regpassword.match(password) == None):
        flash("error in password","warning")
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Invalid login details.', 'danger')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')


    regmail = re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")
    regname = re.compile("^[a-z0-9_-]{3,15}$")
    regpassword = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$")
    
    if(regmail.match(email) == None):
        flash('Error in Email.', 'warning')
        return redirect(url_for('auth.signup'))

    if(regname.match(name) == None):
        flash('Error in name',"warning")
        return redirect(url_for('auth.signup') )         
    
    if(regpassword.match(password)==None):
        flash("Error in password","warning")
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first() 
    if user: 
        flash('Email address already exists.', 'warning')
        return redirect(url_for('auth.login'))
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    flash('Successfully registered. Now you can log in.', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))