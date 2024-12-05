from repository.class_repository import ClassRepository
from models.class_model import ClassModel

class ClassService:
    def __init__(self):
        self.repository = ClassRepository()

    def create_class(self, name, date_time, description, capacity):
        new_class = ClassModel(name, date_time, description, capacity)
        self.repository.save_class(new_class)
        return new_class
