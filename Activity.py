class Activity:
    def __init__(self, date, type, distance, duration, average_speed, info):
        self.date = date  # date of activity, for all types
        self.type = type  # strength, run, bike, ...
        self.distance = distance  # only for some types
        self.duration = duration  # for all types
        self.average_speed = average_speed  # only for some types
        self.info = info  # e.g. interval, indoor, upper body, lower body, ...
