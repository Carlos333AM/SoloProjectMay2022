from flask_app.config.MySQLconnection import connectToMySQL 
import pprint 
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash 


class User: 
    db_name = "gizmos_pizza_db" 
    def __init__(self, data): 
        self.id = data['id'] 

        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.address = data['address'] 
        self.city = data['city'] 
        self.state = data['state'] 
        self.zip_code = data['zip_code'] 

        self.email = data['email'] 
        self.password = data['password'] 
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at'] 


    @classmethod 
    def create_user(cls, data): 
        query = "INSERT INTO users (first_name, last_name, address, city, state, zip_code, email, password) VALUES ( %(first_name)s, %(last_name)s, %(address)s, %(city)s, %(state)s, %(zip_code)s, %(email)s, %(password)s );" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        pprint.pprint(f"RESULTS: {results}") 
        return results 

    @classmethod 
    def show_all_users(cls): 
        query = "SELECT * FROM users;" 
        results = connectToMySQL(cls.db_name).query_db(query) 
        pprint.pprint(f"RESULTS: {results}") 
        return results 

    @classmethod 
    def get_user_by_id(cls, data): 
        query = "SELECT * FROM users WHERE id = %(id)s;" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        this_user = cls(results[0]) 
        pprint.pprint(f"RESULTS: {results}") 
        return this_user 

    @classmethod 
    def get_by_email(cls, data): 
        query = "SELECT * FROM users WHERE email = %(email)s;" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        pprint.pprint(results) 
        if len(results) < 1: 
            return False 
        return cls(results[0]) 

    @classmethod 
    def update_user(cls, data): 
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, address = %(address)s, city = %(city)s, state = %(state)s, zip_code = %(zip_code)s WHERE id = %(id)s ;" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        pprint.pprint(f"RESULTS: {results}") 
        return results 

    @classmethod 
    def delete_user(cls, data): 
        query = "DELETE FROM users WHERE id = %(id)s;" 
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        pprint.pprint(f"RESULTS: {results}") 


    @staticmethod 
    def validate_register(user): 
        is_valid = True 
        query = "SELECT * FROM users WHERE email = %(email)s;" 
        results = connectToMySQL(User.db_name).query_db(query, user) 
        if len(user['first_name']) < 2: 
            flash("First name must be at least 2 letters long.", "register") 
            is_valid = False 
        if len(user['last_name']) < 2: 
            flash("Last name must be at least 2 letters long.", "register") 
            is_valid = False 
        if len(user['address']) < 3: 
            flash("Address must be at least 3 characters long.", "register") 
            is_valid = False 
        if len(user['city']) < 2: 
            flash("City must be at least 2 letters long.", "register") 
            is_valid = False 
        if len(user['city']) < 2: 
            flash("City must be at least 2 letters long.", "register") 
            is_valid = False 
        if results: 
            flash("This email is already used. Please try another.", "register") 
            is_valid = False 
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email. Please try again.", "register") 
            is_valid = False 
        if user['password'] != user['confirm_password']: 
            flash("Passwords don't match. Please try again.", "register") 
            is_valid = False 
        return is_valid 
