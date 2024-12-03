from services.auth_service import AuthService

class AuthController:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def sign_up(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.auth_service.sign_up(username, password)
            print(f"Account created successfully for {user.username}.")
        except ValueError as e:
            print(e)

    def sign_in(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.auth_service.sign_in(username, password)
            print(f"Welcome back, {user.username}!")
        except ValueError as e:
            print(e)
