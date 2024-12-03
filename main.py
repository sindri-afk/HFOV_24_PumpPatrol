from SignInUp.register_user import register_user


def main():
    user = register_user()
    while True:
        print("\n1. View Memberships\n2. Log Out")
        user_choice = input("Select an option: ")

        if user_choice == "1":
            print(f"Memberships for {user.username}")  # Show user profile
        elif user_choice == "2":
            print(f"Goodbye, {user.username}!")
            break  # Breaks the inner loop and returns to main menu
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
