class Yoga:
    def __init__(self):
        self.teacher = "Mr. Myagi"
        self.duration = 60
        self.location = "CityGym Hub"
    
    def get_details(self):
        return f"Yoga class with {self.teacher} \nlocation: {self.location} \nduration: {self.duration} minutes"

class Cardio:
    def __init__(self):
        self.teacher = "Mr. Rocky"
        self.duration = 30
        self.location = "CityGym Hub"
    
    def get_details(self):
        return f"Cardio class with {self.teacher} \nlocation: {self.location} \nduration: {self.duration} minutes and then stretching for {self.duration} minutes"
    
class Crossfit:
    def __init__(self):
        self.teacher = "Mr. Arnold"
        self.duration = 15
        self.location = "CityGym Hub"
    
    def get_details(self):
        return f"Crossfit class with {self.teacher}\nlocation: {self.location} \nduration: 4 sets of {self.duration} minute exercises"
        