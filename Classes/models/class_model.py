
class ClassModel:
    def __init__(self, class_id, name, description, capacity, date_time):
        self.class_id = class_id
        self.name = name
        self.description = description
        self.capacity = capacity
        self.date_time = date_time

    def to_dict(self):
        return {
            "class_id": self.class_id,
            "name": self.name,
            "description": self.description,
            "capacity": self.capacity,
            "date_time": self.date_time,
        }

    @staticmethod
    def from_dict(data):
        return ClassModel(
            class_id=data["class_id"],
            name=data["name"],
            date_time=data["date_time"],
            description=data["description"],
            capacity=data["capacity"],
        )
