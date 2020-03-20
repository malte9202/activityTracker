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
add_activity_label = Label(main_window, text="'Add activity' adds a new activity.")
# info label
info_label = Label(main_window, text="Press 'Quit' to exit the program")
# test label
welcome_label = Label(main_window)
# user input
user_input_ = Entry(main_window, bd=5, width=20)


# add components to the main window with PACK
add_activity_label.grid(row=0, column=0)
user_input.grid(row=0, column=1)
add_activity_button.grid(row=0, column=2)
info_label.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
welcome_label.grid(row=2, column=0, columnspan=3)

# waiting for user input in main loop
main_window.mainloop()
