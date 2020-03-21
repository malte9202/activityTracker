import sqlite3  # import sqlite3 module
from sqlite3 import Error  # import sqlite3 errors
from Activity import Activity  # import activity class

connection = sqlite3.connect("activity_tracker.db")  # enable db connection
cursor = connection.cursor()  # set cursor


def create_table_activities():  # function to create table
    # sql statement to create table activities
    create_table_query = 'CREATE TABLE IF NOT EXISTS activities' \
                         '(date TEXT,' \
                         'type TEXT,' \
                         'distance REAL,' \
                         'duration REAL,' \
                         'average_speed REAL,' \
                         'info TEXT)'
    cursor.execute(create_table_query)  # execute query to create table
    connection.commit()  # commit queries


create_table_activities()  # create table for test


def insert_activity(activity):  # function to insert activity
    insert_query = 'INSERT INTO activities VALUES (?, ?, ?, ?, ?, ?)'  # statement for inserting activities
    # execute insert query
    cursor.execute(insert_query, (activity.date, activity.type, activity.distance,
                                  activity.duration, activity.average_speed, activity.info))
    connection.commit()  # commit queries

# activity_1 = Activity('26.02.2020', 'strength', None, 45, None, 'upper body')  # create test object

# insert_activity(activity_1)  # test insert function

'''
def activity_overview():  # function to show recent activities
    overview_query = 'SELECT * FROM activities LIMIT 10'  # query to show recent activities
    cursor.execute(overview_query)  # execute overview query
    connection.commit()  # commit query
    rows = cursor.fetchall()
    for row in rows:
        print(row)


activity_overview() # call function for test purposes
'''
'''
def search_for_date(date):  # function to search for date
    search_query_date = 'SELECT * FROM activities WHERE date = ? LIMIT 50'  # query to search for date
    cursor.execute(search_query_date, date)  # execute search for date
    connection.commit()  # commit query


def search_for_type(type):  # function to search for type
    search_query_type = 'SELECT * FROM activities WHERE type LIKE ? LIMIT 50'
    cursor.execute(search_query_type, type)
    connection.commit()


def search_for_distance(distance):  # function to search for distance
    search_query_distance = 'SELECT * FROM activities WHERE distance = ? LIMIT 50'
    cursor.execute(search_query_distance, distance)
    connection.commit()


def search_for_duration(duration):  # function to search for duration
    search_query_duration = 'SELECT * FROM activities WHERE duration = ? LIMIT 50'
    cursor.execute(search_query_duration, duration)
    connection.commit()


def search_for_speed(speed):  # function to search for speed
    search_query_speed = 'SELECT * FROM activities WHERE average_speed = ? LIMIT 50'
    cursor.execute(search_query_speed, speed)
    connection.commit()


def search_for_info(info):  # function to search for info
    search_query_info = 'SELECT * FROM activities WHERE info LIKE ? LIMIT 50'
    cursor.execute(search_query_info, info)
    connection.commit()


def order_activities(field):  # function to order results
    order_query = 'SELECT * FROM activities ORDER BY ? LIMIT 50'
    cursor.execute(order_query, field)
    connection.commit()
'''

# connection.close()  # close connection
