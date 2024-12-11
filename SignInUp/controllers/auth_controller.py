from SignInUp.services.auth_service import AuthService
from SignInUp.repositories.user_repository import UserRepository

class AuthController:
    def __init__(self):
        user_repo = UserRepository()
        self.auth_service = AuthService(user_repo)

    def sign_up(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        while True:
            trainer_or_member = input("Are you a trainer? (y/n): ").lower()
            if trainer_or_member in ['y', 'n']:
                break
            else:
             print("Invalid input. Please enter 'y' for yes or 'n' for no.")

        try:
            user = self.auth_service.sign_up(username, password, trainer_or_member)
            print(f"User {user.username} created successfully!")
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
