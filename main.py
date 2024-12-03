import time
from SignInUp.controllers.auth_controller import AuthController

from display import display_menu

user = None
auth_controller = AuthController()


def sign_up():
    auth_controller.sign_up()  # Handled by AuthController
    time.sleep(1)
    main()

def sign_in():
    global user
    user = auth_controller.sign_in()  # Handled by AuthController
    if user:
        print(f"Welcome {user.username}!")
        time.sleep(1)
    else:
        time.sleep(1)
        main()

def main():
    
    # Registering user
    menu_options = {
        1: ("Sign Up", sign_up),
        2: ("Sign In", sign_in),
        3: ("Exit", None),
    }
    display_menu("City Gym Hub", menu_options)

    # User main menu
    if user:
        menu_options = {
            1: ("View Memberships", None),
            2: ("Exit", None),
        }
        display_menu("City Gym Hub", menu_options)


if __name__ == "__main__":
    main()