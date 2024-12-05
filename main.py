import time
from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.services.membership_service import MembershipService
from CreateClass.controllers.class_controller import ClassController  

from display import display_menu

# Initialize services and controllers
user = None
auth_controller = AuthController()
membership_service = MembershipService()
class_controller = ClassController()


def correct_main_menu():
    if user and user.trainer == "y":
        return trainer_main_menu
    return user_main_menu


def view_memberships():
    memberships = membership_service.view_memberships() 
    menu_options = {
        i: (f"{m.name} - ${m.price} for {m.duration}", lambda m_id=m.plan_id: buy_membership(m_id))
        for i, m in enumerate(memberships, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu(f"{user.username}'s City Gym Hub", correct_main_menu()))
    display_menu("Memberships", menu_options)


def buy_membership(plan_id):
    membership_service.buy_membership(plan_id)  
    time.sleep(2)
    display_menu(f"{user.username}'s City Gym Hub", correct_main_menu())


def sign_up():
    auth_controller.sign_up()  
    time.sleep(1)
    main()


def sign_in():
    global user
    user = auth_controller.sign_in() 
    if user:
        print(f"Welcome {user.username}!")
        time.sleep(1)
        display_menu(f"{user.username}'s City Gym Hub", correct_main_menu())
    else:
        time.sleep(1)
        main()


def create_class():
    class_controller.create_class()
    time.sleep(2)
    display_menu(f"{user.username}'s City Gym Hub", correct_main_menu())


# Menus
start_screen = {
    1: ("Sign Up", sign_up),
    2: ("Sign In", sign_in),
    3: ("Exit", None),
}

user_main_menu = {
    1: ("View Memberships", view_memberships),
    2: ("Exit", None),
}

trainer_main_menu = {
    1: ("View Memberships", view_memberships),
    2: ("Create Class", create_class), 
    3: ("Exit", None),
}


def main():
    """Main function to display the initial menu."""
    display_menu("City Gym Hub", start_screen)


if __name__ == "__main__":
    main()
