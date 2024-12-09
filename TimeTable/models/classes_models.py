class Yoga:
    def __init__(self):
        self.instructor = "Mr. Myagi"
        self.duration = 60
        self.location = "City Gym Yoga Studio"
    
    def get_class_info(self):
        return f"Class: Yoga class with {self.instructor}\nDuration: {self.duration} minutes \nLocation: {self.location}"
    
class Crossfit:
    def __init__(self):
        self.instructor = "Mr. T"
        self.duration = 30
        self.location = "City Gym Crossfit Studio"
    
    def get_class_info(self):
        return f"Class: Crossfit class with {self.instructor}\nDuration: 2 sets of{self.duration} minute workouts \nLocation: {self.location}"
    
class Cardio:
    def __init__(self):
        self.instructor = "Mr. Rocky"
        self.duration = 30
        self.location = "City Gym Cardio Studio"
    
    def get_class_info(self):
        return f"Class: Cardio class with {self.instructor}\nDuration: {self.duration} minutes cardio and {self.duration} stretching\nLocation: {self.location}"
