# import tkinter module
from tkinter import *

# import everything from the data file
from data import *

# create main window
window = Tk()

# set title for window
window.title("ActivityTracker by malte9202")

# create intro label
main_label = Label(window, text="Enter the following activity data")

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
main_label.grid(row=0, column=0, columnspan=2)  # info label
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
# exit button
exit_button.grid(row=7, column=3)

# waiting for user input in main loop
window.mainloop()

