from SignInUp.services.auth_service import AuthService
from SignInUp.repositories.user_repository import UserRepository

class AuthController:
    def __init__(self):
        user_repo = UserRepository()
        self.auth_service = AuthService(user_repo)

    def sign_up(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.auth_service.sign_up(username, password)
            print(f"User {user.username} signed up successfully!")
        except ValueError as e:
            print(e)

    def sign_in(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.auth_service.sign_in(username, password)
            return user  # Returning the signed-in user
        except ValueError as e:
            print(e)
            return None  # Return None if sign-in failed
