import time
from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.services.membership_service import MembershipService
from controllers.class_controller import ClassController  # Import the new ClassController

from display import display_menu

# Global variables
user = None
auth_controller = AuthController()
membership_service = MembershipService()
class_controller = ClassController()  # Initialize ClassController

# Define functions for menu actions
def view_memberships():
    memberships = membership_service.view_memberships()  # Handled by MembershipService
    menu_options = {
        i: (f"{m.name} - ${m.price} for {m.duration}", lambda m_id=m.plan_id: buy_membership(m_id))
        for i, m in enumerate(memberships, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu("City Gym Hub", user_main_menu))
    display_menu("Memberships", menu_options)

def buy_membership(plan_id):
    membership_service.buy_membership(plan_id)  # Handled by MembershipService
    time.sleep(2)
    display_menu("City Gym Hub", user_main_menu)

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

# Define menus
start_screen = {
    1: ("Sign Up", sign_up),
    2: ("Sign In", sign_in),
    3: ("Exit", None),
}

user_main_menu = {
    1: ("View Memberships", view_memberships),
    2: ("Create Class", class_controller.create_class),  # Add the Create Class action
    3: ("Exit", None),
}

# Main function
def main():
    # Display the start screen
    display_menu("City Gym Hub", start_screen)

    # Display user main menu after signing in
    if user:
        display_menu(f"{user.username}'s City Gym Hub", user_main_menu)

# Entry point
if __name__ == "__main__":
    main()
