from Classes.repository.class_repository import ClassRepository
from Classes.models.class_model import ClassModel
from SignInUp.repositories.user_repository import UserRepository

class ClassService:
    def __init__(self):
        self.class_repository = ClassRepository()
        self.user_repository = UserRepository()

    def create_class(self, name, description, capacity, date_time):
        next_class_id = self.class_repository.get_next_class_id()
        new_class = ClassModel(class_id=next_class_id, name=name, description=description,
                               capacity=capacity, date_time=date_time)

        self.class_repository.save_class(new_class)
        return new_class
    
    def book_class(self, user_id, class_id):
        class_to_book = self.class_repository.get_class_by_id(class_id)
        if not class_to_book:
            raise ValueError("Class not found!")

        users = self.user_repository.load_users()
        user = next((u for u in users if u.user_id == user_id), None)

        if class_id in user.classes:
            raise ValueError("You have already booked this class!")

        user.classes.append(class_id)
        class_to_book.capacity -= 1

        self.user_repository.save_users(users)
        self.class_repository.save_class(class_to_book)

        print(f"You have successfully booked class {class_to_book.name}")