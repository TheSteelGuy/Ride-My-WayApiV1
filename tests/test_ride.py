'''test ride views'''
from flask_testing import TestCase
from flask import request
import unittest
import json
from api import create_app
from api.tables import create_test_ride_table


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
        create_test_ride_table()
        self.ride = {
            'destination': 'testdestination',
            'date': '21-10-2018',
            'time': '10.00 am',
            'meetpoint': 'kasarani',
            'charges': '900'
        }

        self.signup_user = {
            'username': 'collo',
            'phone': '0723-222-3333',
            'password': '12345',
            'confirm': '12345'
        }

        JOIN_RIDE_URL = 'api/v1/rides/1/requests'
        JOIN_RIDE_REQUESTER = {
            'phone_contact': '0723-1111-2222',
            'destination': 'kisumu'
            'rideid': '1'
        }
        REQUEST = self.client.post(
            JOIN_RIDE_URL,
            data=json.dumps(JOIN_RIDE_REQUESTER),
            content_type='application/json'
        )

        self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(self.signup),
            content_type='application/json')
        token = json.loads(signup().data.decode())['token']
        HEADERS = {
            'Authorization': 'Bearer ' + token
        }

    def tearDown(self):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE ride_tests")
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def post_ride_helper(self):
        ''' helper method to create a ride for testcases'''
        ride_response = self.client.post(
            'api/v1/users/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        return ride_response

    def test_ride_creation(self):
        '''test if a user can create a ride offer'''
        ride = self.client.post(
            'api/v1/user/rides',
            data=json.dumps(self.ride),
            content_type='application/json',
            headers=HEADERS
        )
        self.assertEqual(ride.status_code, 201)
        self.assertIn('succefully logged in', str(ride.data))

    def test_fetch_a_single_ride(self):
        '''tests a single ride retrival'''
        self.client.post(
            '/api/v1/users/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        ride = self.client.get(
            'api/v1/rides/1',
            content_type='application/json'
        )
        self.assertEqual(ride.status_code, 200)

    def test_join_ride_request(self):
        '''tests if a user can join a ride'''
        ride = self.help_post_ride()
        join_ride = self.client.post(
            'api/v1/rides/1/requests',
            content_type='application/json',
            headers=HEADERS
        )
        res = json.loads(join_ride.data.decode())
        self.assertIn(
            'you have succefully sent a join request, you will receive notification soon',
            res['message'])

    def test_cancel_ride_offer(self):
        '''tests if a user can cancel a ride they offered'''
        ride = self.help_post_ride()
        cancel_ride = self.client.delete(
            'api/v1/rides/1/cancel',
            content_type='application/json',
            headers=HEADERS
        )
        res = json.loads(cancel_ride.data.decode())
        self.assertEqual(len(res), 1)

    def test_reject_ride_request(self):
        '''tests if a user can reject a ride request for offer they created'''
        ride = self.help_post_ride()

        reject_ride = self.client.put(
            'api/v1/users/rides/1/requests/1',
            data=({'status': 'rejected'})
            content_type='application/json',
            headers=HEADERS
        )
        self.assertIn(
            'your request for this ride was rejected', str(
                reject_ride.data))

    def test_accept_ride_request(self):
        '''tests if a user can reject a ride request for offer they created'''
        ride = self.help_post_ride()

        accept_ride = self.client.put(
            'api/v1/users/rides/1/requests/1',
            data=({'status': 'accepted'})
            content_type='application/json',
            headers=HEADERS
        )
        self.assertIn(
            'your request for this ride was accepted', str(
                accept_ride.data))

    def test_get_rides(self):
        '''tests fetching all rides'''
        self.client.post(
            '/api/v1/users/rides',
            data=json.dumps(self.ride),
            content_type='application/json'
        )
        rides = self.client.get(
            'api/v1/rides',
            content_type='application/json'
        )
        res = json.loads(rides.data.decode())
        self.assertEqual(len(res), 1)

    def test_get_ride_requests(self):
        '''tests fetching all rides'''
        requets_to_join_ride = self.client.get(
            '/users/rides/1/requests',
            content_type='application/json',
            headers=HEADERSs
        )
        res = json.loads(requests_to_join.data.decode())
        self.assertTrue(len(res) == 1)


if __name__ == '__main__':
    unittest.main()
