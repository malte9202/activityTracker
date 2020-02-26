import sqlite3
from sqlite3 import Error
from Activity import Activity

connection = sqlite3.connect("activity_tracker.db")
cursor = connection.cursor()

create_table_activities = 'CREATE TABLE IF NOT EXISTS activities' \
                          '(id INTEGER PRIMARY KEY,' \
                          'date TEXT,' \
                          'type TEXT,' \
                          'distance REAL,' \
                          'duration REAL,' \
                          'average_speed REAL,' \
                          'additional_info TEXT)'

cursor.execute(create_table_activities)

activity_insert = 'INSERT INTO activities VALUES (?, ?, ?, ?, ?, ?, ?)'

activity_1 = Activity('2020-02-25', 'strength', None, 61, None, 'mixed')

cursor.execute(activity_insert, (23, activity_1.date, activity_1.type, activity_1.distance, activity_1.duration, activity_1.average_speed, activity_1.info))

#cursor.execute(activity_insert, (1, '2020-02-24', 'run', 10, 60, 10, 'indoor'))

cursor.execute("SELECT * FROM activities LIMIT 20")

connection.commit()

print(cursor.fetchall())

connection.commit()

connection.close()