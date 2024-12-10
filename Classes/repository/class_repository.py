import json
from ..models.class_model import ClassModel

class ClassRepository:
    def __init__(self, file_path="Classes/data/classes.json"):
        self.file_path = file_path

    def load_classes(self):
        try:
            with open(self.file_path, "r") as file:
                return [ClassModel.from_dict(item) for item in json.load(file)]
        except FileNotFoundError:
            return []

    def save_class(self, class_instance):
        classes = self.load_classes()
        classes.append(class_instance)
        with open(self.file_path, "w") as file:
            json.dump([c.to_dict() for c in classes], file, indent = 4)

    def get_next_class_id(self):
        classes = self.load_classes()
        if not classes:
            return 1
        return max(c.class_id for c in classes) + 1
    
    def get_class_by_id(self, class_id):
        classes = self.load_classes()
        return next((c for c in classes if c.class_id == class_id), None)
