"""
User class. Contains the relevant methods for the user class
"""
import re


class User():
    '''a base pssanger class from which a driver can be made'''

    def __init__(self, name, phone, password, confirm_p):
        ''' constructor method to give a user its attributes'''
        self.name = name
        self.phone = phone
        self.password = password
        self.confirm_p = confirm_p

    @classmethod
    def verify_password(cls, pwd, c_pwd):
        '''verifies if the password and confirm pass matches'''
        if pwd == c_pwd:
            return True
        return False

    @classmethod
    def serialize_user(cls, user_object):
        ''' takes a user object and returns its dict representation'''
        return dict(
            username=user_object.name,
            phone=user_object.phone,
            password=user_object.password,
        )

    @staticmethod
    def check_phone(phone):
        '''checks if a username meets ceratin threshhlolds'''
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
    def does_user_exist(cls, users, phone_contact):
        ''' find out if user exist meant to reduce the number and areas of for looping'''
        user_ = list(
            filter(
                lambda user_dict: user_dict['phone'] == phone_contact,
                users))
        if user_:
            return True
        return False
