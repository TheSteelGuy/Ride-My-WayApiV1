'''test auth views'''
import psycopg2
import unittest
import json
from flask_testing import TestCase
from flask import request
from api import create_app

from api.tables import create_test_user_table


class ParentTest (unittest.TestCase):
    def create_app(self):
        '''pass testing enviroment'''
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        ''' prepare tests'''
        self.conn = psycopg2.connect(
            database='rmwtests',
            user='adminride',
            host='localhost',
            password='ridemyway1')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        create_test_user_table()
        self.client = self.app.test_client()
        self.signup_user = {
            'username': 'collo',
            'phone': '0723-222-3333',
            'password': '12345',
            'confirm': '12345'
        }
        self.login_user = {
            'username': 'collo',
            'password': '12345'
        }

        SIGNUP_URL = 'api/v1/auth/signup'
        signup = self.client.post(
            SIGNUP_URL,
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )

    def tearDown(self):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE users")
        self.conn.commit()
        self.conn.close()


class TestAuthentication(ParentTest):
    '''tests user authentication endpoints'''

    def test_signup_more_than_once(self):
        """test if a user can signup twice with the same details"""
        response = self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )
        self.assertIn(str(response.data),
                      'you have already registered, login please')

    def test_logout(self):
        """tests_user logout"""

        signup = self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(self.signup_user),
            content_type='application/json'
        )
        self.assertEqual(signup.status_code, 201)
        self.data_ = json.loads(signup.data.decode())
        self.assertEqual(self.data_['message'], 'registration successfull')

        logout = self.client.post(
            'auth/api/v1/logout',
            headers={
                'Authorization': 'Bearer ' + json.loads(
                    register.data.decode()
                )['token'],
            },
            content_type='application/json'
        )
        res = json.loads(logout.data.decode())
        self.assertIn('you have successfully logged out', res['message'])

    def test_if_user_can_signin(self):
        '''tests if a user can log in with correct credentials'''
        login = self.client.post(
            'api/v1/auth/signin',
            data=json.dumps(self.login_user),
            content_type='application/json'
        )
        self.assertIn('you have succefully logged in', str(login.data))


if __name__ == '__main__':
    unittest.main()
