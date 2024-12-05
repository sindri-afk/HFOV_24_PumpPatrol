from ..services.class_service import ClassService

class ClassController:
    def __init__(self):
        self.service = ClassService()

    def create_class(self):
        print("Enter Class Details:")

        name = input("Class Name: ")
        date_time = input("Date and Time (YYYY-MM-DD HH:MM): ")
        description = input("Description: ")

        
        while True:
            try:
                capacity = int(input("Capacity: "))
                if capacity <= 0:
                    print("Capacity must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for capacity.")

        
        new_class = self.service.create_class(name, date_time, description, capacity)
        print(f"Class '{new_class.name}' created successfully!")
