
# queries for ordering by each db field
order_activity_by_date = 'SELECT * FROM activities ORDER BY date LIMIT 10'
order_activity_by_type = 'SELECT * FROM activities ORDER BY type LIMIT 10'
order_activity_by_distance = 'SELECT * FROM activities ORDER BY distance LIMIT 10'
order_activity_by_duration = 'SELECT * FROM activities ORDER BY duration LIMIT 10'
order_activity_by_speed = 'SELECT * FROM activities ORDER BY average_speed LIMIT 10'
order_activity_by_info = 'SELECT * FROM activities ORDER BY additional_info LIMIT 10'

connection.commit()  # commit queries

print(cursor.fetchall())  # fetch all results

connection.commit()

connection.close()