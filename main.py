from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.controllers.membership_controller import MembershipController

def main():
    auth_controller = AuthController()
    membership_controller = MembershipController()

    while True:
        print("\n1. Sign Up\n2. Sign In\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            auth_controller.sign_up()  # Handled by AuthController
        elif choice == "2":
            user = auth_controller.sign_in()  # Handled by AuthController
            if user:  # If sign-in was successful
                print(f"Welcome back, {user.username}!")
                while True:
                    print("\n1. View Memberships\n2. Buy Membership\n3. View Profile\n4. Log Out")
                    user_choice = input("Select an option: ")

                    if user_choice == "1":
                        print("\nAvailable Memberships:")
                        membership_controller.view_memberships()  # Display all memberships
                    elif user_choice == "2":
                        plan_id = int(input("Enter the Plan ID to purchase: "))
                        membership_controller.buy_membership(plan_id)  # Handle membership purchase
                    elif user_choice == "3":
                        print(f"Profile for {user.username}")  # Display user profile
                    elif user_choice == "4":
                        print(f"Goodbye, {user.username}!")
                        break  # Log out and return to the main menu
                    else:
                        print("Invalid option. Try again.")
        elif choice == "3":
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()