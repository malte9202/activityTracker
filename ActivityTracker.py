# App to track different kinds of activities
# Activities can be entered manually via GUI
# Activities are saved in SQLite DB

import sqlite3  # import sqlite 3 module
from tkinter import *  # import tkinter for gui
from Activity import *  # import activity class

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


# test function for button action
def convert_user_input_to_object():
    # date, type and duration are mandatory
    date_to_save = input_date.get()
    type_to_save = input_type.get()
    duration_to_save = float(input_duration.get())
    # check if average speed is empty and set null if it is empty, if it is not empty convert to float
    if input_average_speed.get() == "":
        average_speed_to_save = None
    else:
        average_speed_to_save = float(input_average_speed.get())
    # info is optional and anything can be entered, but check if empty to set null
    if input_info.get() == "":
        info_to_save = None
    else:
        info_to_save = input_info.get()
    # check if distance is empty and set null, otherwise convert to float
    if input_distance.get() == "":
        distance_to_save = None
    else:
        distance_to_save = float(input_distance.get())
    # create activity_to_save object with user input values
    activity_to_save = Activity(date_to_save, type_to_save, distance_to_save,
                                duration_to_save,average_speed_to_save, info_to_save)
    # check if date, type and duration are not empty because they are mandatory, raise ValueError if empty
    if date_to_save == "" or type_to_save == "" or duration_to_save == "":
        raise ValueError
    else:
        return activity_to_save


# function to save activity
def save_activity():
    try:
        convert_user_input_to_object()  # convert user input to object
        insert_activity(convert_user_input_to_object())  # insert object into database
        saved_label = Label(window, text="activity saved! You can enter another activity.")
        saved_label.grid(row=7, column=0)
        input_date.delete(0, 255)
        input_type.delete(0, 255)
        input_distance.delete(0, 255)
        input_duration.delete(0, 255)
        input_average_speed.delete(0, 255)
        input_info.delete(0, 255)
    except ValueError:
        intro_label.config(text="please enter valid values for the mandatory fields (marked with *)")


# create program flow and graphical user interface

window = Tk()  # create main window
window.title("ActivityTracker")  # set title for the window

# create database table
create_table_activities()

# create intro label
intro_label = Label(window, text="Enter information about your activity. Fields marked with * are mandatory.")

# create labels for each input field
date_label = Label(window, text="Date*")
type_label = Label(window, text="Type*")
distance_label = Label(window, text="Distance")
duration_label = Label(window, text="Duration*")
average_speed_label = Label(window, text="Average speed")
info_label = Label(window, text="Info")

# get user input for each attribute of the activity object
input_date = Entry(window, bd=3, width=15)
input_type = Entry(window, bd=3, width=15)
input_distance = Entry(window, bd=3, width=15)
input_duration = Entry(window, bd=3, width=15)
input_average_speed = Entry(window, bd=3, width=15)
input_info = Entry(window, bd=3, width=15)

# create buttons
exit_button = Button(window, text="Quit", command=window.quit)
save_activity_button = Button(window, text="Save activity", command=save_activity)

# add components to the window in grid mode
intro_label.grid(row=0, column=0, columnspan=2)  # info label
# date elements
date_label.grid(row=1, column=0)
input_date.grid(row=1, column=1)
# type elements
type_label.grid(row=2, column=0)
input_type.grid(row=2, column=1)
# distance elements
distance_label.grid(row=3, column=0)
input_distance.grid(row=3, column=1)
# duration elements
duration_label.grid(row=4, column=0)
input_duration.grid(row=4, column=1)
# average speed elements
average_speed_label.grid(row=5, column=0)
input_average_speed.grid(row=5, column=1)
# info elements
info_label.grid(row=6, column=0)
input_info.grid(row=6, column=1)
# add activity button
save_activity_button.grid(row=7, column=1)
# exit button
exit_button.grid(row=7, column=3)

# waiting for user input in main loop
window.mainloop()