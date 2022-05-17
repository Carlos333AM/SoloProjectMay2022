from flask_app.config.MySQLconnection import connectToMySQL 
from flask_app import app 
from crypt import methods
from flask_app.models.order import Order 
from flask_app.models.user import User 
from flask import render_template, redirect, request, session 



@app.route('/gizmospizza/menu') 
def menu_page(): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza') 
    return render_template('menu.html', order = Order.show_all_orders()) 

@app.route('/gizmospizza/create-order', methods = ['POST']) 
def create_order_page(): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza') 
    order_info = { 
        "pizza_type" : request.form['pizza_type'], 
        "pizza_size" : request.form['pizza_size'], 
        "pizza_quantity" : request.form['pizza_quantity'], 

        "soda" : request.form['soda'], 
        "soda_size" : request.form['soda_size'], 
        "soda_quantity" : request.form['soda_quantity'], 

        "fruit_drink" : request.form['fruit_drink'], 
        "fruit_drink_size" : request.form['fruit_drink_size'], 
        "fruit_drink_quantity" : request.form['fruit_drink_quantity'], 

        "milk_shake" : request.form['milk_shake'], 
        "milk_shake_size" : request.form['milk_shake_size'], 
        "milk_shake_quantity" : request.form['milk_shake_quantity'], 

        "ice_cream" : request.form['ice_cream'], 
        "ice_cream_quantity" : request.form['ice_cream_quantity'], 

        "brownie" : request.form['brownie'], 
        "brownie_quantity" : request.form['brownie_quantity'], 

        "cake" : request.form['cake'], 
        "cake_quantity" : request.form['cake_quantity'], 
        "user_id" : session['user_id']
    } 
    id = Order.create_order(order_info) 
    session['order_id'] = id 
    return redirect(f'/gizmospizza/cart/{id}') 

@app.route('/gizmospizza/delete-order-item/<int:id>') 
def destroy_order_item(id): 
    if 'user_id' not in session: 
        return redirect('/gizmospizza/logout') 
    order_info = { 
        "id" : id 
    } 
    Order.delete_order(order_info) 
    return redirect('/gizmospizza/menu') 
