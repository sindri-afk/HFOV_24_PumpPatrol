# main.py
from services.auth_service import AuthService
from repositories.user_repository import UserRepository

def main():
    user_repo = UserRepository()
    auth_service = AuthService(user_repo)

    while True:
        print("\n1. Sign Up\n2. Sign In\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                user = auth_service.sign_up(username, password)
                print(f"User {user.username} signed up successfully!")
            except ValueError as e:
                print(e)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                user = auth_service.sign_in(username, password)
                print(f"Welcome back, {user.username}!")
            except ValueError as e:
                print(e)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
