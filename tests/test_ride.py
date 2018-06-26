'''test ride views'''
from flask_testing import TestCase
from flask import request
import unittest
import json
from api import create_app
from api.Ride.views import rides


class Testbase(TestCase):
    """parent class"""

    def create_app(self):
        self.app = create_app('testing')
        return self.app

    def setUp(self):
        self.client = self.app.test_client()
        self.ride = {
            'destination': 'testdestination',
            'date':'22-11-2019',
            'time': '9.00 am',
            'meetpoint': 'testmeetpoint',
            'charges': '200'
        }

    def tearDown(self):
        '''make the user list empty after each test case'''
        del rides[:]

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
        self.assertEqual(ride.status_code,201)
    
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
        self.assertEqual(len(res),1)

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
        self.assertEqual(ride.status_code, 200)

    def test_join_ride(self):
        '''tests if a user can join a ride'''
        ride = self.help_post_ride()
        join_ride =self.client.post(
            'api/v1/rides/1/requests',
            content_type='application/json'
        )
        res = json.loads(join_ride.data.decode())
        self.assertIn('you have succefully sent a join request, you will receive notification soon',res['message'])
    
    def test_cancel_ride(self):
        '''tests if a user can cancel a ride'''
        ride = self.help_post_ride()
        cancel_ride = self.client.delete(
            'api/v1/rides/1/cancel',
            content_type='application/json'
        )
        res = json.loads(cancel_ride.data.decode())
        self.assertEqual(len(res),1)

if __name__ == '__main__':
    unittest.main()
