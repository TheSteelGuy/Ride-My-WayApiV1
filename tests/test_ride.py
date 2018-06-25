'''test ride views'''
from flask_testing import TestCase
from flask import request
import unittest
import json
from api import create_app


class Testbase(TestCase):
    """parent class"""

    def create_app(self):
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        self.client = self.app.test_client()
        self.ride = {
            'destination': 'testdestination',
            'date':'22/11/2018',
            'time': '9.00 am',
            'meetpoint': 'testmeetpoint',
            'charges': '200'
        }

    def tearDown(self):
        '''make the user list empty after each test case'''
        rides = list()

    def help_post_ride(self):
        ''' help post a ride for testcase'''
        ride_response = self.client.post(
            'api/v1/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        return ride_response

    def test_create_ride(self):
        '''test if a user can create a ride offer'''
        ride = self.client.post(
            'api/v1/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        self.assertTrue(ride.status_code==201)
    
    def test_get_rides(self):
        '''tests getting a ride by id'''
        self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        rides = self.client.get(
            'api/v1/rides',
            content_type='application/json'
        )
        res = json.loads(rides.data.decode())
        self.assertIn('testdestination', res['destination'])

    def test_get_ride(self):
        '''tests rides retrival'''
        self.client.post(
            '/api/v1/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        ride = self.client.get(
            'api/v1/rides/1',
            content_type='application/json'
        )
        self.assertEqual(ride.data,'')

    def test_join_ride(self):
        '''tests if a user can join a ride'''
        ride = self.help_post_ride()
        user_details = {
            'username':'testuser',
            'phone':'0734252525'
        }
        self.client.post(
            'api/v1/rides/1/requests',
            data=json.dumps(user_details),
            content_type='application/json'
        )


if __name__ == '__main__':
    unittest.main()
