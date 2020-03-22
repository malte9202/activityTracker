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