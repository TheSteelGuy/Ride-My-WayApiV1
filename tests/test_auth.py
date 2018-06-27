'''test auth views'''
from flask_testing import TestCase
from flask import request
import unittest 
import json
from api import create_app
from api.Auth.views import users

class Testbase(TestCase):
    '''parent class for all test cases'''
    def create_app(self):
        '''pass testing enviroment'''
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        ''' prepare test cases'''
        self.client = self.app.test_client()
        self.signup_user={
            'username':'collo',
            'phone': '0723-222-3333',
            'password':'12345',
            'confirm':'12345'
        }
        self.login_user={
            'username':'collo',
            'password':'12345'
        }
        URL = 'api/v1/auth/signup'
        signup = self.client.post(
            URL,
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )


    def tearDown(self):
        '''clear any saved data after each test'''
        del users[:]



class TestAuth(Testbase):
    '''tests user authentication endpoints'''
    def test_signup_twice(self):
        """test if a user can signup twice with the same details"""
        response = self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)


    def test_login_possible(self):
        '''tests if a user can log in with correct credentials'''
        self.client.post(
           'api/v1/auth/signup',
           data=json.dumps(self.signup_user),
           content_type='application/json'
        )
        login = self.client.post(
            'api/v1/auth/signin',
            data=json.dumps(self.login_user),
            content_type='application/json'
        )
        self.assertIn('you have succefully logged in', str(login.data)) 


    def test_logout_possible(self):
        '''tests if a user can logout'''
        logout = self.client.post(
            'api/v1/auth/logout',
            content_type='application/json'
        )
        res = json.loads(logout.data.decode())
        self.assertIn('succesfully logged out', res['message'])

if __name__ == '__main__':
    unittest.main()

