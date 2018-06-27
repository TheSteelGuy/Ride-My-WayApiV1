'''ride class. Contains the methods for this class'''


class Ride():
    '''ride class'''

    def __init__(self, destination, date, time, meetpoint, charges):
        ''' constructor method to give a user object its attributes'''
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
            ride_id=id_count,
            owner_id='owner_id' #this will be  taken care of by jwt.for now there is no way of passing it
        )

    @staticmethod
    def check_destination(phone):
        '''validates destination'''
        pass

    @classmethod
    def does_ride_exist(cls, rides, destination, time):
        ''' find out if a ride exist'''
        destination = list(
            filter(
                lambda ride_dict: ride_dict['destination'] == destination,
                rides))
        time = list(filter(lambda ride_dict: ride_dict['time'] == time, rides))
        if time and destination:
            return True
        return False

    @classmethod
    def get_ride(cls, rides, ride_id):
        ''' retrieve a ride based on id'''
        ride = list(
            filter(
                lambda ride_dict: ride_dict['ride_id'] == ride_id,
                rides))
        if ride:
            return ride
        return False
