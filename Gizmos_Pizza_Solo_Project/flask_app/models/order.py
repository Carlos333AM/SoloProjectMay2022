from flask_app.config.MySQLconnection import connectToMySQL 
from flask_app import app 
from flask_app.models.user import User 
from flask_app.models import user 
from flask import flash 
import pprint 


class Order: 
    db_name = "gizmos_pizza_db" 
    def __init__(self, data): 
        self.id = data['id'] 

        self.pizza_type = data['pizza_type'] 
        self.pizza_size = data['pizza_size'] 
        self.pizza_quantity = data['pizza_quantity'] 

        self.soda = data['soda'] 
        self.soda_size = data['soda_size'] 
        self.soda_quantity = data['soda_quantity'] 

        self.fruit_drink = data['fruit_drink'] 
        self.fruit_drink_size = data['fruit_drink_size'] 
        self.fruit_drink_quantity = data['fruit_drink_quantity'] 

        self.milk_shake = data['milk_shake'] 
        self.milk_shake_size = data['milk_shake_size'] 
        self.milk_shake_quantity = data['milk_shake_quantity'] 

        self.ice_cream = data['ice_cream'] 
        self.ice_cream_quantity = data['ice_cream_quantity'] 

        self.brownie = data['brownie'] 
        self.brownie_quantity = data['brownie_quantity'] 

        self.cake = data['cake'] 
        self.cake_quantity = data['cake_quantity'] 

        self.creator = None 


    @classmethod 
    def create_order(cls, data): 
        query = "INSERT INTO orders ( pizza_type, pizza_size, pizza_quantity, soda, soda_size, soda_quantity, fruit_drink, fruit_drink_size, fruit_drink_quantity, milk_shake, milk_shake_size, milk_shake_quantity, ice_cream, ice_cream_quantity, brownie, brownie_quantity, cake, cake_quantity, user_id ) VALUES ( %(pizza_type)s, %(pizza_size)s, %(pizza_quantity)s, %(soda)s, %(soda_size)s, %(soda_quantity)s, %(fruit_drink)s, %(fruit_drink_size)s, %(fruit_drink_quantity)s, %(milk_shake)s, %(milk_shake_size)s, %(milk_shake_quantity)s, %(ice_cream)s, %(ice_cream_quantity)s, %(brownie)s, %(brownie_quantity)s, %(cake)s, %(cake_quantity)s, %(user_id)s );" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        pprint.pprint(f"RESULTS: {results}") 
        return results 

    @classmethod 
    def get_order_by_id(cls, data): 
        query = "SELECT * FROM orders WHERE id = %(id)s ;" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        print(results)
        return cls(results[0]) 

    @classmethod 
    def show_all_orders(cls): 
        query = "SELECT * FROM orders;" 
        results = connectToMySQL(cls.db_name).query_db(query) 
        pprint.pprint(f"RESULTS: {results}") 
        return results 

    @classmethod 
    def delete_order(cls, data): 
        query = "DELETE FROM orders WHERE id = %(id)s;" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        pprint.pprint(f"RESULTS: {results}") 
