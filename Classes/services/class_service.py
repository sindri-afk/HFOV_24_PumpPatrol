from Classes.repository.class_repository import ClassRepository
from Classes.models.class_model import ClassModel

class ClassService:
    def __init__(self):
        self.repository = ClassRepository()

    def create_class(self, name, description, capacity, date_time):
        new_class = ClassModel(name, description, capacity, date_time)
        self.repository.save_class(new_class)
        return new_class
