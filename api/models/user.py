"""
User class. Contains the relevant methods for the user class
"""
from datetime import datetime, timedelta
import re
import jwt
from flask import current_app
from api.tables import CONN


class User():
    '''handles a user object'''

    def __init__(self, name, phone, password, confirm_p):
        ''' constructor method to give a user its attributes'''
        self.name = name
        self.phone = phone
        self.password = password
        self.confirm_p = confirm_p

    def save_user(self):
        ''' saves user in the table'''
        cursor = CONN.cursor()
        sql_query = 'INSERT INTO users (username, phone_contact, password) VALUES(%s,%s,%s)'
        user_tuple = (self.name, self.phone,self.password)
        cursor.execute(sql_query,user_tuple)
        CONN.commit()

    @classmethod
    def verify_password(cls, pwd, c_pwd):
        '''verifies if the password and confirm password matches'''
        if pwd == c_pwd:
            return True
        return False

    @staticmethod
    def generate_token(user_id):
        "method which generates token for users"
        try:
             paylod = {
                 'exp':datetime.utcnow() + timedelta(minutes=120),
                 'iat':datetime.utcnow(),
                 'sub':user_id

             }
             encoded_token = jwt.encode(
                 paylod,current_app.config['SECRET_KEY']
             )
             return encoded_token

        except Exception as e:
                string = 'An exception of type {0} occurred. Arguments:\n{1!r}'
                message = string.format(type(e).__name__, e.args)
                return message

    @staticmethod
    def decode_token(token_auth):
        '''decodes the token'''
        try:
            paylod = jwt.decode(
                token_auth,current_app.config.get('SECRET_KEY'))
            token_blacklisted = BlacklistTokens.verify_token(token_auth)
            if token_blacklisted:
                return 'seems like you have already logged out, login again'
            return paylod['sub']
        except jwt.ExpiredSignatureError:
            return 'token expired, you need to login again'
        except jwt.InvalidTokenError:
            return 'this token was altered, its is not authentic'


    @staticmethod
    def check_phone(phone):
        '''checks if a phone contact follows a certain pattern'''
        regex = "\w{3}-\w{3}-\w{4}"
        if re.search(regex, phone):
            if phone[0] != 0 and phone[1] != 7:
                return True
        return False

    @staticmethod
    def p_strength(password):
        '''check passphrase strength'''
        if len(password.strip()) < 1:
            return 'password cannot be empty, please provide a password'
        if len(password) < 4:
            return 'password should be more than 5 characters long'
        return True

    @classmethod
    def does_user_exist(cls, phone):
        ''' find out if a user exist before adding to db'''
        sql_query = 'SELECT phone_contact FROM users WHERE phone_contact =%s'
        cursor = CONN.cursor()
        cursor.execute(sql_query,(phone,))
        rows = cursor.fetchall()
        if rows:
            return True
        return False

class BlacklistTokens():
    '''blacklist token'''
    def __init__(self, token):
        '''contructor for token'''
        self.token = token

    @staticmethod
    def verify_token(auth_token):
        '''
        Checks if the token exist in the database,
        that is wether it is blacklisted or not.
        '''
        sql_query = 'SELECT token FROM blacklist_tokens WHERE token =%s'
        cursor = CONN.cursor()
        cursor.execute(sql_query,(str(auth_token),))
        blacklisted_token = cursor.fetchone()
        if blacklisted_token:
            return True
        return False

    
    def save_token(self,token):
        ''' saves user in the table'''
        cursor = CONN.cursor()
        sql_query = 'INSERT INTO blacklist_tokens (tokens) VALUES (%s)'
        cursor.execute(sql_query,(token))
        CONN.commit()