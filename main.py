import time
from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.services.membership_service import MembershipService
from Classes.controllers.class_controller import ClassController  
from VirtualPrograms.services.virtualworkout_service import VirtualWorkoutService
from TrackWorkoutHistoryandProgress.workout_controller import track_exercise, view_exercise_history
from Classes.repository.class_repository import ClassRepository
from Classes.services.class_service import ClassService

from display import display_menu

# Initialize services and controllers
user = None
auth_controller = AuthController()
membership_service = MembershipService()
class_controller = ClassController()
workouts = VirtualWorkoutService()
class_repo = ClassRepository()
class_service = ClassService()


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
    menu_options[len(menu_options) + 1] = ("Membership Plans Information", lambda: display_menu("Membership Information", membership_info))
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu()))
    display_menu("Memberships", menu_options)

def buy_membership(plan_id):
    global user
    membership_service.buy_membership(user.user_id, plan_id)  # Handled by MembershipService
    time.sleep(4)
    display_menu("City Gym Hub", correct_main_menu())

def view_current_membership_plan():
    global user
    membership_service.get_user_membership(user.user_id)
    time.sleep(4)
    display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu())

def display_workout_program(workouts):
    for workout in workouts:
        print(f"Program Name: {workout.program_name}\n")
        print(f"Description:\n{workout.program_description}\n")
    input("Press Enter to go back to the menu.")
    view_virtual_workout_programs()


def view_virtual_workout_programs():
    workout = workouts.view_workout_programs()
    menu_options = {
        i: (workout.program_name, lambda w=workout: display_workout_program([w]))
        for i, workout in enumerate(workout, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu()))
    display_menu("Workout Programs", menu_options)

def track_workout_history_and_progress(user):
    workout_menu = {
        1: ("Track Exercise", lambda: track_exercise(user, track_workout_history_and_progress)),
        2: ("View Exercise History", lambda: view_exercise_history(user, track_workout_history_and_progress)),
        3: ("Go back", lambda: display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu()))  # Call correct_main_menu() here
    }
    display_menu("Workout History and Progress", workout_menu)

def book_class(class_id):
    global user
    class_service.book_class(user.user_id, class_id) # Handled by MembershipService
    time.sleep(4)
    display_menu("City Gym Hub", correct_main_menu())


def view_classes():
    classes = class_repo.load_classes()
    menu_options = {
        i: ((str(c.name) + ' ----- ' + str(c.date_time)), lambda c=c: display_classes([c]))
        for i, c in enumerate(classes, 1)
    }
    menu_options[len(menu_options) + 1] = ("Go back", lambda: display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu()))
    display_menu("Classes", menu_options)


def display_classes(classes):
    for c in classes:
        print(f"Class Name: {c.name}")
        print(f"Description: {c.description}")
        print(f"Capacity: {c.capacity}")
        print(f"Date and Time: {c.date_time}")
        print()

    while True:
        user_input = input("Do you want to book this class? (y/n): ").strip().lower()
        if user_input == "y":
            if c.class_id in user.classes:
                print("You have already booked this class!")
                time.sleep(2)
                view_classes()
                break
            book_class(c.class_id)
            break
        
        elif user_input == "n":
            view_classes()

        else: 
            print("Invalid input, please enter either 'y' or 'n'!")
            continue

def sign_up():
    auth_controller.sign_up()  
    time.sleep(1)
    main()


def sign_in():
    global user
    user = auth_controller.sign_in() 
    if user:
        print(f"Welcome {(user.username).capitalize()}!")
        time.sleep(1)
        display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu())
    else:
        time.sleep(1)
        main()


def create_class():
    class_controller.create_class()
    time.sleep(2)
    display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu())


# Menus
start_screen = {
    1: ("Sign Up", sign_up),
    2: ("Sign In", sign_in),
    3: ("Exit", None),
}

user_main_menu = {
    1: ("View All Membership Plans", view_memberships),
    2: ("View Your Membership Plan", view_current_membership_plan),
    3: ("View Virtual Workout Programs", view_virtual_workout_programs),
    4: ("View and Book Classes", view_classes),
    5: ("Track Workout History and Progress", lambda: track_workout_history_and_progress(user)),
    6: ("Exit", None),
}

trainer_main_menu = {
    1: ("View All Membership Plans", view_memberships),
    2: ("View Your Membership Plan", view_current_membership_plan),
    3: ("View Virtual Workout Programs", view_virtual_workout_programs),
    4: ("View and Book Classes", view_classes),
    5: ("Track Workout History and Progress", lambda: track_workout_history_and_progress(user)),
    6: ("Create Class", create_class), 
    7: ("Exit", None),
}

membership_info = {
        1: ("The Basic Plan provides access to the main gym hall "
            "and all equipment and machines there.", None),
        2: ("The Premium Plan provides the same amenities as "
            "the Basic Plan while also giving you acces to "
            "our many classes we have, for example, CrossFit, "
            "Yoga and Pilates. The Premium Plan also gives you access "
            "to our spa area with a sauna, a cold tub and a hot tub.", None),
        3: ("Go back.", view_memberships)
        }


def main():
    """Main function to display the initial menu."""
    display_menu("City Gym Hub", start_screen)


if __name__ == "__main__":
    main()
