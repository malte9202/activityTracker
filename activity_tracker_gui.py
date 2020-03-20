# import tkinter module
from tkinter import *


def add_activity():
    entry_text = user_input.get()
    if entry_text == "":
        welcome_label.config(text="Gib zuerst etwas ein.")
    else:
        entry_text = "Welcome " + entry_text
        welcome_label.config(text=entry_text)


# set main window
main_window = Tk()
# define title for main window
main_window.title("ActivityTracker by malte9202")

# create label and buttons
# button to add a new activity
add_activity_button = Button(main_window, text="Add activity", command=add_activity)
# exit button
exit_button = Button(main_window, text="Quit", command=main_window.quit)
# label for adding an activity
add_activity_label = Label(main_window, text="Enter the following activity information")
# labels for each input field
input_date_label = Label(main_window, text="Date")
input_type_label = Label(main_window, text="Type")
input_distance_label = Label(main_window, text="Distance")
input_duration_label = Label(main_window, text="Duration")
input_average_speed_label = Label(main_window, text="Average Speed")
input_info_label = Label(main_window, text="Info")
# info label
info_label = Label(main_window, text="Press 'Quit' to exit the program")
# test label
welcome_label = Label(main_window)
# user input for each attribute of the activity object
user_input_date = Entry(main_window, bd=3, width=15)
user_input_type = Entry(main_window, bd=3, width=15)
user_input_distance = Entry(main_window, bd=3, width=15)
user_input_duration = Entry(main_window, bd=3, width=15)
user_input_average_speed = Entry(main_window, bd=3, width=15)
user_input_info = Entry(main_window, bd=3, width=15)


# add components to the main window with PACK
add_activity_label.grid(row=0, column=0)
input_date_label.grid(row=1, column=0)
user_input_date.grid(row=1, column=1)
input_type_label.grid(row=2, column=0)
user_input_type.grid(row=2, column=1)
input_distance_label.grid(row=3, column=0)
user_input_distance.grid(row=3, column=1)
input_duration_label.grid(row=4, column=0)
user_input_duration.grid(row=4, column=1)
input_average_speed_label.grid(row=5, column=0)
user_input_average_speed.grid(row=5, column=1)
input_info_label.grid(row=6, column=0)
user_input_info.grid(row=6, column=1)
add_activity_button.grid(row=0, column=2)
exit_button.grid(row=7, column=3)
welcome_label.grid(row=2, column=0, columnspan=3)

# waiting for user input in main loop
main_window.mainloop()
