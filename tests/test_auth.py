'''test auth views'''
from flask_testing import TestCase
from flask import request
import unittest 
import json
from api import create_app
from api.Auth.views import users

class Testbase(TestCase):
    """parent class"""
    def create_app(self):
        self.app = create_app('testing')
        return self.app

    def setUp(self):
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
        URL = 'auth/api/v1/signup'
        signup = self.client.post(
            URL,
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )


    def tearDown(self):
        del users[:]



class TestAuth(Testbase):
    '''tests user authentication methods'''
    def test_signup_twice(self):
        """test registaration"""
        response = self.client.post(
            'auth/api/v1/signup',
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)


    def test_login(self):
        '''tests if a user can log in'''
        self.client.post(
           'auth/api/v1/signup',
           data=json.dumps(self.signup_user),
           content_type='application/json'
        )
        login = self.client.post(
            'auth/api/v1/signin',
            data=json.dumps(self.login_user),
            content_type='application/json'
        )
        self.assertIn('you have succefully logged in', str(login.data)) 


    def test_logout(self):
        '''tests_user logout'''
        logout = self.client.post(
            'auth/api/v1/logout',
            content_type='application/json'
        )
        res = json.loads(logout.data.decode())
        self.assertIn('succesfully logged out', res['message'])

if __name__ == '__main__':
    unittest.main()

