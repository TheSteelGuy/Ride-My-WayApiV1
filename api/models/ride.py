'''ride.py'''
from datetime import datetime, date
import re

class Ride():
    '''ride class'''

    def __init__(self, destination, date, time, meetpoint, charges):
        ''' constructor method to give a user its attributes'''
        self.destination = destination
        self.date = date
        self.time = time
        self.meetpoint = meetpoint
        self.charges = charges



    @classmethod
    def serialize_ride(cls, ride_object):
        ''' takes a user object and returns its dict representation'''
        return dict(
            destination=ride_object.destination,
            date=ride_object.date,
            time=ride_object.time,
            meetpoint=ride_object.meetpoint,
            charges=ride_object.charges
        )

    @staticmethod
    def check_destination(phone):
        '''validates destination'''
        pass
    