from ..services.class_service import ClassService
from ..repository.class_repository import ClassRepository

class ClassController:
    def __init__(self):
        self.service = ClassService()
        self.repository = ClassRepository()

    def get_input_or_cancel(self, prompt):
        user_input = input(prompt).strip()
        if user_input.lower() == "cancel":
            print("Are you sure you want to cancel class creation? (y/n)")
            if input().strip().lower() == "y":
                print("Class creation cancelled.")
                return None
            else:
                return self.get_input_or_cancel(prompt)
        return user_input

    def create_class(self):
        print("Enter Class Details:")
        print("Type 'cancel' at any time to cancel class creation.\n")

        name = self.get_input_or_cancel("Class Name: ")
        if name is None: return

        description = self.get_input_or_cancel("Description: ")
        if description is None: return

        while True:
            capacity = self.get_input_or_cancel("Capacity: ")
            if capacity is None:  # User canceled
                return
            try:
                capacity = int(capacity)
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid integer or type 'cancel' to cancel.")
        
        date_time = self.get_input_or_cancel("Date and Time (YYYY-MM-DD HH:MM): ")
        if date_time is None: return

        new_class = self.service.create_class(name, description, capacity, date_time)
        print(f"Class '{new_class.name}' created successfully!")
    

