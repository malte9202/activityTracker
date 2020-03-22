# App to track different kinds of activities
# Activities can be entered manually via GUI
# Activities are saved in SQLite DB

import sqlite3  # import sqlite 3 module
from tkinter import *  # import tkinter for gui

connection = sqlite3.connect("activity_tracker.db")  # enable db connection
cursor = connection.cursor()  # set cursor


# function to create the activities table
def create_table_activities():
    # sql statement to create table activities
    create_table_query = 'CREATE TABLE IF NOT EXISTS activities' \
                         '(date TEXT,' \
                         'type TEXT,' \
                         'distance REAL,' \
                         'duration REAL,' \
                         'average_speed REAL,' \
                         'info TEXT);'
    cursor.execute(create_table_query)  # execute query to create table
    connection.commit()  # commit query


# function to insert an activity into the activities table
def insert_activity(activity):
    insert_query = 'INSERT INTO activities VALUES (?, ?, ?, ?, ?, ?);'  # statement for inserting activities
    # execute insert query with values from an Activity object
    cursor.execute(insert_query, (activity.date, activity.type, activity.distance, activity.duration,
                                  activity.average_speed, activity.info))
    connection.commit()  # commit query


# create program flow and graphical user interface

window = Tk()  # create main window
window.title("ActivityTracker")  # set title for the window

# create intro label
intro_label = Label(window, text="Enter information about your activity")

# create labels for each input field
date_label = Label(window, text="Date")
type_label = Label(window, text="Type")
distance_label = Label(window, text="Distance")
duration_label = Label(window, text="Duration")
average_speed_label = Label(window, text="Average speed")
info_label = Label(window, text="Info")

# get user input for each attribute of the activity object
input_date = Entry(window, bd=3, width=15)
input_type = Entry(window, bd=3, width=15)
input_distance = Entry(window, bd=3, width=15)
input_duration = Entry(window, bd=3, width=15)
input_average_speed = Entry(window, bd=3, width=15)
input_info = Entry(window, bd=3, width=15)