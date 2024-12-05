from ..services.class_service import ClassService

class ClassController:
    def __init__(self):
        self.service = ClassService()

    def create_class(self):
        print("Enter Class Details:")

        name = input("Class Name: ")
        description = input("Description: ")
        capacity = int(input("Capacity: "))
        date_time = input("Date and Time (YYYY-MM-DD HH:MM): ")

        new_class = self.service.create_class(name, description, capacity, date_time)
        print(f"Class '{new_class.name}' created successfully!")
