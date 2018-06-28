'''ride class. Contains the methods for this class'''

from api.tables import CONN


class Ride():
    '''ride class'''

    def __init__(self, destination, date, time, meetpoint, charges,creator_id):
        ''' constructor method to give a user object its attributes'''
        self.destination = destination
        self.date = date
        self.time = time
        self.meetpoint = meetpoint
        self.charges = charges
        self.creator = creator_id

    def save_ride(self, ride_tuple):
        ''' save ride in the table'''
        cursor = CONN.cursor()
        sql_query = 'INSERT INTO rides (destination,date,departure_time,meetpoint,fare_charges,creator_id) VALUES(%s,%s, %s,%s,%s,%s)'
        cursor.execute(sql_query,ride_tuple)
        CONN.commit()



    @classmethod
    def serialize_ride(cls, ride_object, id_count):
        ''' takes a user object and returns its dict representation'''
        sql_query = 'SELECT * FROM rides'
        cursor = CONN.cursor()
        cursor.execute(sql_query)

        return dict(
            destination=ride_object.destination,
            date=ride_object.date,
            time=ride_object.time,
            meetpoint=ride_object.meetpoint,
            charges=ride_object.charges,
            ride_id=id_count,
            owner_id='owner_id'
        )
    @staticmethod
    def delete_ride(id):
        ''' retrieve a ride based on id'''
        sql_query = 'DELETE FROM rides where id = %s'
        cursor = CONN.cursor()
        cursor.execute(sql_query,(id,))
        row = cursor.fetchone()
        if row:
            return False
        return True

    @staticmethod
    def check_destination(phone):
        '''validates destination'''
        pass

    @classmethod
    def does_ride_exist(cls, dest, time):
        ''' find out if a ride exist'''
        sql_query = 'SELECT departure_time, destination FROM rides WHERE destination =%s AND departure_time =%s'
        cursor = CONN.cursor()
        cursor.execute(sql_query,(dest, time))
        rows = cursor.fetchall()
        if rows:
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