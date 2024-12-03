# repositories/user_repository.py
import json
from models.user import User

class UserRepository:
    def __init__(self, db_path="SignInUp/data/users.json"):
        self.db_path = db_path

    def load_users(self):
        try:
            with open(self.db_path, 'r') as file:
                data = json.load(file)
                return [User(**user) for user in data]
        except FileNotFoundError:
            return []

    def save_users(self, users):
        with open(self.db_path, 'w') as file:
            json.dump([user.__dict__ for user in users], file)

    def find_by_username(self, username):
        users = self.load_users()
        return next((user for user in users if user.username == username), None)

    def add_user(self, user):
        users = self.load_users()
        users.append(user)
        self.save_users(users)
