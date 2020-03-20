# import tkinter module
from tkinter import *

# import everything from the data file
from data import *

# create main window
window = Tk()

# set title for window
window.title("ActivityTracker by malte9202")

# create intro label
info_label = Label(window, text="Enter the following activity data")

# create labels for each input field
date_label = Label(window, text="Date")
type_label = Label(window, text="Type")
distance_label = Label(window, text="Distance")
duration_label = Label(window, text="Duration")
average_speed_label = Label(window, text="Average speed")
info_label = Label(window, text="Info")

# create buttons
exit_button = Button(window, text="Quit", command=window.quit())
# add_activity_button = Button(window, text="Add activity", command=insert_activity)

# get user input for each attribute of the activity object
input_date = Entry(window, bd=3, width=15)
input_type = Entry(window, bd=3, width=15)
input_distance = Entry(window, bd=3, width=15)
input_duration = Entry(window, bd=3, width=15)
input_average_speed = Entry(window, bd=3, width=15)
input_info = Entry(window, bd=3, width=15)

# add components to the window in grid mode
