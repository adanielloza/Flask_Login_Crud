# routes.py
from flask import Blueprint, render_template, redirect, url_for, jsonify, request, flash
from flask_login import login_required, login_user
from werkzeug.security import check_password_hash
from controllers.user import add_user_function, edit_user_function, delete_user_function
from models.user import User
import sys

main = Blueprint('main', __name__) #routename = main

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(email=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('main.login'))

        login_user(user)
        return redirect(url_for('main.home'))

    return render_template('login.html')

@main.route('/CRUD', methods=['GET'])
@login_required
def home():
    data = User.get_all()
    return render_template('CRUD.html', data=data)

@main.route('/adduser', methods=['GET','POST'])

def add_user():
    data = add_user_function()
    print (data, file=sys.stderr)
    return render_template('adduser.html',data=data)

@main.route('/edituser/<int:id>', methods=['GET','POST'])
@login_required
def edit_user(id):
    user = User.get_by_id(id)
    print(user.id)
    data = edit_user_function(user)
    return render_template('edituser.html', user=user, data=data)

@main.route('/deleteuser/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    user = User.get_by_id(id)
    print (user, file=sys.stderr)
    delete_user_function(user)
    return redirect(url_for('main.home'))

