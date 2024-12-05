class Yoga:
    def __init__(self):
        self.teacher = "Mr. Myagi"
        self.duration = 60
        self.location = "CityGym Hub"
    
    def get_details(self):
        return f"Yoga class with {self.teacher} \nLocation: {self.location} \nDuration: {self.duration} minutes\n"

class Cardio:
    def __init__(self):
        self.teacher = "Mr. Rocky"
        self.duration = 30
        self.location = "CityGym Hub"
    
    def get_details(self):
        return f"Cardio class with {self.teacher} \nLocation: {self.location} \nDuration: {self.duration} minutes and then stretching for {self.duration} minutes\n"
    
class Crossfit:
    def __init__(self):
        self.teacher = "Mr. Arnold"
        self.duration = 15
        self.location = "CityGym Hub"
    
    def get_details(self):
        return f"Crossfit class with {self.teacher}\nLocation: {self.location} \nDuration: 4 sets of {self.duration} minute exercises\n"
        