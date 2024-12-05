import time
from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.services.membership_service import MembershipService
from VirtualPrograms.services.virtualworkout_service import VirtualWorkoutService
from VirtualPrograms.models.workout_display import display_workout_program
from display import display_menu

# Global variables
user = None
auth_controller = AuthController()
membership_service = MembershipService()
workouts = VirtualWorkoutService()


def view_memberships():
    """
    Displays the membership options and allows users to buy memberships.
    """
    memberships = membership_service.view_memberships()  # Handled by MembershipService
    menu_options = {
        i: (f"{m.name} - ${m.price} for {m.duration}", lambda m_id=m.plan_id: buy_membership(m_id))
        for i, m in enumerate(memberships, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu("City Gym Hub", user_main_menu))
    display_menu("Memberships", menu_options)


def buy_membership(plan_id):
    """
    Allows the user to buy a membership.
    """
    membership_service.buy_membership(plan_id)  # Handled by MembershipService
    time.sleep(2)
    display_menu("City Gym Hub", user_main_menu)


def view_virtual_workout_programs():
    workout = workouts.view_workout_programs()
    menu_options = {
        i: (workout.program_name, lambda w=workout: display_workout_program([w]))
        for i, workout in enumerate(workout, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu(f"{user.username}'s City Gym Hub", user_main_menu))
    display_menu("Workout Programs", menu_options)


def sign_up():
    """
    Handles user registration.
    """
    auth_controller.sign_up()  # Handled by AuthController
    time.sleep(1)
    main()


def sign_in():
    """
    Handles user login.
    """
    global user
    user = auth_controller.sign_in()  # Handled by AuthController
    if user:
        print(f"Welcome {user.username}!")
        time.sleep(1)
    else:
        time.sleep(1)
        main()


# Menu definitions
start_screen = {
    1: ("Sign Up", sign_up),
    2: ("Sign In", sign_in),
    3: ("Exit", None),
}

user_main_menu = {
    1: ("View Memberships", view_memberships),
    2: ("View Virtual Workout Programs", view_virtual_workout_programs),
    3: ("Exit", None),
}


def main():
    """
    Main entry point for the application.
    """
    display_menu("City Gym Hub", start_screen)  # Display start screen

    if user:  # If user is logged in, display the main menu
        display_menu(f"{user.username}'s City Gym Hub", user_main_menu)


if __name__ == "__main__":
    main()