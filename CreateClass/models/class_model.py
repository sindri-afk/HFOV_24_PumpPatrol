import uuid
from datetime import datetime

class ClassModel:
    def __init__(self, name, date_time, description, capacity):
        self.class_id = str(uuid.uuid4())
        self.name = name
        self.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        self.description = description
        self.capacity = capacity

    def to_dict(self):
        return {
            "class_id": self.class_id,
            "name": self.name,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M"),
            "description": self.description,
            "capacity": self.capacity,
        }

    @staticmethod
    def from_dict(data):
        return ClassModel(
            name=data["name"],
            date_time=data["date_time"],
            description=data["description"],
            capacity=data["capacity"],
        )
