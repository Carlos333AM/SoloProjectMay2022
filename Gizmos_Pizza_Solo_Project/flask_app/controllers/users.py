from crypt import methods
from pprint import pprint
from flask_app import app 
from flask_app.config.MySQLconnection import connectToMySQL
from flask_app.models.order import Order 
from flask_app.models.user import User 
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 
from flask import flash 
from flask import render_template, redirect, request, session, flash 


@app.route('/gizmospizza') 
def register_login_page(): 
    return render_template('register_login.html') 

@app.route('/gizmospizza/create-user', methods = ['POST']) 
def create_new_user(): 
    if not User.validate_register(request.form): 
        return redirect('/gizmospizza') 
    user_info = { 
        "first_name" : request.form['first_name'], 
        "last_name" : request.form['last_name'], 
        "address" : request.form['address'], 
        "city" : request.form['city'], 
        "state" : request.form['state'], 
        "zip_code" : request.form['zip_code'], 
        "email" : request.form['email'], 
        "password" : bcrypt.generate_password_hash(request.form['password']) 
    } 
    id = User.create_user(user_info) 
    session['user_id'] = id 
    return redirect('/gizmospizza/menu') 

@app.route('/gizmospizza/login', methods = ['POST']) 
def login_page(): 
    user = User.get_by_email(request.form) 
    if not user: 
        flash("Invalid Email or Password", "login")
        return redirect('/gizmospizza') 
    session['user_id'] = user.id 
    print(session) 
    return redirect('/gizmospizza/menu') 

@app.route('/gizmospizza/user/<int:id>') 
def show_one_user(id): 
    user_select = { 
        "id" : id 
    } 
    this_user = User.get_user_by_id(user_select) 
    return render_template('account.html', one_user = this_user) 

@app.route('/gizmospizza/edit/<int:id>')
def edit_user(id): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza/logout') 
    user_select = { 
        "id" : id 
    } 
    this_user = User.get_user_by_id(user_select) 
    return render_template('update_page.html', user = User.get_user_by_id(user_select)) 

@app.route('/gizmospizza/update/<int:id>', methods = ['POST']) 
def update_user_info(id): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza/logout') 
    user_info = { 
        "first_name" : request.form['first_name'], 
        "last_name" : request.form['last_name'], 
        "address" : request.form['address'], 
        "city" : request.form['city'], 
        "state" : request.form['state'], 
        "zip_code" : request.form['zip_code'], 
        "id" : id
    } 
    User.update_user(user_info) 
    return redirect('/gizmospizza/account') 

@app.route('/gizmospizza/account') 
def account_page(): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza') 
    user_info = { 
        "id" : session['user_id'] 
    }
    return render_template('account.html', user = User.get_user_by_id(user_info)) 

@app.route('/gizmospizza/cart/<int:id>') 
def cart_page(id): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza') 
    user_info = { 
        "id" : session['user_id'] 
    } 
    order_info = { 
        "id" : id 
    } 
    this_order = Order.get_order_by_id(order_info) 
    print(this_order) 
    return render_template('cart.html', user = User.get_user_by_id(user_info), order = Order.get_order_by_id(order_info)) 

@app.route('/gizmospizza/delete-user/<int:id>') 
def destroy_user_account(id): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza/logout') 
    user_info = { 
        "id" : id 
    } 
    User.delete_user(user_info) 
    return redirect('/gizmospizza') 

@app.route('/gizmospizza/logout') 
def logout(): 
    session.clear() 
    return redirect('/gizmospizza') 
