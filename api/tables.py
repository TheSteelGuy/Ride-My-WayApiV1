''' module function that creates a user table'''

import psycopg2

CONN = psycopg2.connect(database='ridemyway', user='adminride', host='localhost', password='ridemyway1')
# conn = psycopg2.connect(database='rmwtests', user='adminride', host='localhost', password='ridemyway1')                   


def create_user_table():
    user_table = (
    """
    CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(40),
            phone_contact VARCHAR(20),
            password VARCHAR(164))
    """)
    cursor = CONN.cursor()
    cursor.execute(user_table)
    CONN.commit()
    return True

def create_ride_table():
    '''create tables for rides'''

    ride_table = (
    """
    CREATE TABLE rides (
            id SERIAL PRIMARY KEY,
            destination VARCHAR(64),
            ride_date VARCHAR(40),
            departure_time VARCHAR(10),
            meetpoint VARCHAR(64) ,
            fare_charges INTEGER,
            creator_id INTEGER REFERENCES users (id))
    """)
    cursor = CONN.cursor()
    cursor.execute(ride_table)
    CONN.commit()
    return True

def create_join_req_table():
    join_ = (
    """
    CREATE TABLE ride_joins(
            id SERIAL PRIMARY KEY,
            phone_contact VARCHAR(20),
            ride_id INTEGER REFERENCES rides (id)
            )
    """)
    cursor = CONN.cursor()
    cursor.execute(join_)
    CONN.commit()
    return True
