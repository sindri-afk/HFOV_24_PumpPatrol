import time
from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.services.membership_service import MembershipService
from CreateClass.controllers.class_controller import ClassController  

from display import display_menu


user = None
auth_controller = AuthController()
membership_service = MembershipService()
class_controller = ClassController()  


def view_memberships():
    memberships = membership_service.view_memberships() 
    menu_options = {
        i: (f"{m.name} - ${m.price} for {m.duration}", lambda m_id=m.plan_id: buy_membership(m_id))
        for i, m in enumerate(memberships, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu("City Gym Hub", user_main_menu))
    display_menu("Memberships", menu_options)

def buy_membership(plan_id):
    membership_service.buy_membership(plan_id)  
    time.sleep(2)
    display_menu("City Gym Hub", user_main_menu)

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
    else:
        time.sleep(1)
        main()


start_screen = {
    1: ("Sign Up", sign_up),
    2: ("Sign In", sign_in),
    3: ("Exit", None),
}

user_main_menu = {
    1: ("View Memberships", view_memberships),
    2: ("Create Class", class_controller.create_class), 
    3: ("Exit", None),
}


def main():
    
    display_menu("City Gym Hub", start_screen)

    
    if user:
        display_menu(f"{user.username}'s City Gym Hub", user_main_menu)


if __name__ == "__main__":
    main()
