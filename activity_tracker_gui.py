
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
add_activity_button.grid(row=7, column=0)
exit_button.grid(row=7, column=3)
welcome_label.grid(row=2, column=0, columnspan=3)

# waiting for user input in main loop
main_window.mainloop()

# temporary activity used for db insert
temp_activity = Activity(user_input_date, user_input_type, user_input_distance, user_input_duration,
                         user_input_average_speed, user_input_info)