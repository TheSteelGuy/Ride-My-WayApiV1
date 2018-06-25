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
    def serialize_ride(cls, ride_object, id_count):
        ''' takes a user object and returns its dict representation'''
        return dict(
            destination=ride_object.destination,
            date=ride_object.date,
            time=ride_object.time,
            meetpoint=ride_object.meetpoint,
            charges=ride_object.charges,
            ride_id=id_count
        )

    @staticmethod
    def check_destination(phone):
        '''validates destination'''
        pass

    @classmethod
    def does_ride_exist(cls, rides, destination, time):
        ''' find out if user exist meant to reduce the number and areas of for looping'''
        destination = list(filter(lambda ride_dict:ride_dict['destination']==destination, rides))
        time = list(filter(lambda ride_dict:ride_dict['time']==time, rides))
        if time and destination:
            return True
        return False
    