from services.class_service import ClassService

class ClassController:
    def __init__(self):
        self.service = ClassService()

    def create_class(self):
        print("Enter Class Details:")
        name = input("Class Name: ")
        date_time = input("Date and Time (YYYY-MM-DD HH:MM): ")
        description = input("Description: ")
        capacity = int(input("Capacity: "))

        new_class = self.service.create_class(name, date_time, description, capacity)
        print(f"Class '{new_class.name}' created successfully!")
