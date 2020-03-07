# import tkinter module
from tkinter import *


def test_action():
    print("Test")


# set main window
main_window = Tk()
# define title for main window
main_window.title("ActivityTracker by malte9202")

# create label and buttons
# button to add a new activity
add_activity_button = Button(main_window, text="Add activity", command=test_action)
# exit button
exit_button = Button(main_window, text="Quit", command=main_window.quit)
# label for adding an activity
add_activity_label = Label(main_window, text="'Add activity' adds a new activity.")
# info label
info_label = Label(main_window, text="Some Information\n Press 'Quit' to exit the program")


# add components to the main window with PACK
add_activity_label.pack()
add_activity_button.pack()
info_label.pack()
exit_button.pack()

# waiting for user input in main loop
main_window.mainloop()
