''' module function that creates a user table'''

import psycopg2

CONN = psycopg2.connect(database='ridemyway', user='adminride', host='localhost', password='ridemyway1')
# conn = psycopg2.connect(database='rmwtests', user='adminride', host='localhost', password='ridemyway1')                   

def create_test_ride_table():
    '''create tables'''

    ride_table = (
    """
    CREATE TABLE ride_tests (
            id SERIAL PRIMARY KEY,
            destination VARCHAR(64),
            ride_date VARCHAR(40),
            departure_time VARCHAR(10),
            meetpoint VARCHAR(64) ,
            phone_contact INTEGER,
            fare_charges FLOAT)
    """)
    cursor = CONN.cursor()
    cursor.execute(ride_table)
    CONN.commit()
    cursor.close()
    CONN.close()
    return 'action executed succefully'

def create_test_user_table():
    ride_table = (
    """
    CREATE TABLE user_tests(
            id SERIAL PRIMARY KEY,
            username VARCHAR(40),
            phone VARCHAR(10),
            password VARCHAR(64),
            confirm_pwd VARCHAR(24))
    """)
