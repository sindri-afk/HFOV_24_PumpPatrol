from SignInUp.controllers.auth_controller import AuthController

def register_user():
    auth_controller = AuthController()

    while True:
        print("\n1. Sign Up\n2. Sign In\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            auth_controller.sign_up()  # Handled by AuthController
        elif choice == "2":
            user = auth_controller.sign_in()  # Handled by AuthController
            if user:  # If sign-in was successful
                print(f"Welcome back, {user.username}!")
                return user

        elif choice == "3":
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Invalid option. Try again.")