from classes_model import Yoga, CrossFit, Cardio

class Inspection:
    def __init__(self, class_id):
        self.class_id = class_id

    def get_class_id(self):
        try:
            if self.class_id == "Yoga":
                yoga = Yoga()
                return yoga.get_class_info()
            elif self.class_id == "CrossFit":
                crossfit = CrossFit()
                return crossfit.get_class_info()
            elif self.class_id == "Cardio":
                cardio = Cardio()
                return cardio.get_class_info()
        except ValueError:
            return "Invalid class id"
    