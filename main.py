from SignInUp.controllers.auth_controller import AuthController

def main():
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
                # Add any further functionality here after sign-in
                # For example, we can add a restricted area or additional options
                while True:
                    print("\n1. View Profile\n2. Log Out")
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        print(f"Profile for {user.username}")  # Show user profile
                    elif user_choice == "2":
                        print(f"Goodbye, {user.username}!")
                        break  # Breaks the inner loop and returns to main menu
                    else:
                        print("Invalid option. Try again.")

        elif choice == "3":
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
