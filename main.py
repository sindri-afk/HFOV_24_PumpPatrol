import time
from SignInUp.controllers.auth_controller import AuthController
from MembershipPlan.services.membership_service import MembershipService
from Classes.controllers.class_controller import ClassController  
from VirtualPrograms.services.virtualworkout_service import VirtualWorkoutService
from Classes.repository.class_repository import ClassRepository
from Classes.services.class_service import ClassService
from TrackWorkoutHistoryandProgress.workout_controller import track_exercise, view_exercise_history

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

def book_class(class_id):
    global user
    class_service.book_class(user.user_id, class_id)
    # Refresh the user data from the repository
    users = class_service.user_repository.load_users()
    user = next((u for u in users if u.user_id == user.user_id), None)
    time.sleep(1)
    input("Press any key to continue... ")
    view_classes()

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
        # loaded_classes = class_repo.load_classes()
        user_input = input("Do you want to book this class? (y/n): ").strip().lower()
        if user_input == "y":
            if c.class_id in user.classes:
                print("You have already booked this class!")
                time.sleep(1)
                input("Press any key to continue... ")
                view_classes()
                break
            book_class(c.class_id)
            break
        
        elif user_input == "n":
            print("Booking cancelled!")
            time.sleep(1)
            input("Press any key to continue... ")
            view_classes()
            break

        else: 
            print("Invalid input, please enter either 'y' or 'n'!")
            continue


def view_memberships():
    memberships = {
        1: ("Class Plan", view_class_plan),
        2: ("Gym Plan", view_gym_plan),
        3: ("Full Plan", view_full_plan),
        4: ("Guest Trial", view_guest_trial),
        5: ("Go back", view_memberships_menu)  # Same as requested
    }
    display_menu("Memberships Plans", memberships)

def buy_membership(plan_name, type_name, price, duration):
    global user

    # Get the user's current membership status
    user_membership = membership_service.get_user_membership(user.username)

    # Check if the user already has any membership
    if user_membership:
        # If user already has a membership, prevent purchasing "Guest Trial" again
        if plan_name == "Guest Trial":
            buy_membership_info = {
                "Error": ("The 'Guest Trial' is only available for new users       and cannot be purchased", view_memberships_menu),
                0: ("Press 0 to go back to the memberships menu", view_memberships_menu)
            }
            display_menu("Membership Purchase Confirmation", buy_membership_info)
        else:
            # Proceed with purchasing other memberships
            membership_service.buy_membership(user.username, plan_name, type_name, price, duration)
            
            # Prepare the result information to display in the menu format
            buy_membership_info = {
                "Membership successfully purchased for user": (user.username, view_memberships_menu),
                "Plan": (plan_name, view_memberships_menu),
                "Type": (type_name, view_memberships_menu),
                "Price": (f"${price}", view_memberships_menu),
                "Duration": (duration, view_memberships_menu),
                0: ("Press 0 to go back to the memberships menu", view_memberships_menu)
            }

            display_menu("Membership Purchase Confirmation", buy_membership_info)

    else:
        # If the user does not have any membership, allow them to proceed with purchasing any plan
        membership_service.buy_membership(user.username, plan_name, type_name, price, duration)
        
        # Prepare the result information to display in the menu format
        buy_membership_info = {
            "Membership successfully purchased for user": (user.username, view_memberships_menu),
            "Plan": (plan_name, view_memberships_menu),
            "Type": (type_name, view_memberships_menu),
            "Price": (f"${price}", view_memberships_menu),
            "Duration": (duration, view_memberships_menu),
            0: ("Press 0 to go back to the memberships menu", view_memberships_menu)
        }

        # Display the menu for successful purchase
        display_menu("Membership Purchase Confirmation", buy_membership_info)

    # Wait for user input before returning to the membership menu
    input()
    view_memberships_menu()



def view_current_membership_plan():
    """Displays the user's current membership plan in a structured menu format."""
    global user
    user_membership = membership_service.get_user_membership(user.username)

    if user_membership:
        # Prepare membership information as a dictionary for display
        current_membership_plan_info = {
            "Plan Name": (user_membership['plan_name'], view_memberships_menu),
            "Type": (user_membership['type_name'], view_memberships_menu),
            "Price": (f"${user_membership['price']}", view_memberships_menu),
            "Duration": (user_membership['duration'], view_memberships_menu),
            0: ("Press 0 to go back to the memberships menu", view_memberships_menu)
        }
        display_menu("Your Current Membership Plan", current_membership_plan_info)
    else:
        print("You have not purchased a membership plan yet!")


def view_guest_trial():
    guest_trial_menu = {
        1: ("Guest-Trial: Free for 1 week", lambda: buy_membership("Guest Trial", "", "Free", "1 week")),
        2: ("Go Back", view_memberships),
    }
    display_menu("Guest Trial Membership", guest_trial_menu)

def view_full_short():
    full_short_menu = {
        1: ("1 month for 10.0$", lambda: buy_membership("Full Plan", "Short-Term", "10.0", "1 month")),
        2: ("3 months for 20.0$", lambda: buy_membership("Full Plan", "Short-Term", "20.0", "3 months")),
        3: ("6 months for 30.0$", lambda: buy_membership("Full Plan", "Short-Term", "30.0", "6 months")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Full Plan - Short-Term Membership", full_short_menu)

def view_full_long():
    full_long_menu = {
        1: ("1 year for 50.0$", lambda: buy_membership("Full Plan", "Long-Term", "50.0", "1 year")),
        2: ("2 years for 90.0$", lambda: buy_membership("Full Plan", "Long-Term", "90.0", "2 years")),
        3: ("5 years for 200.0$", lambda: buy_membership("Full Plan", "Long-Term", "200.0", "5 years")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Full Plan - Long-Term Membership", full_long_menu)

def view_full_payg():
    full_payg_menu = {
        1: ("1 time for 15.0$", lambda: buy_membership("Full Plan", "Pay-As-You-Go", "15.0", "1 time")),
        2: ("5 times for 60.0$", lambda: buy_membership("Full Plan", "Pay-As-You-Go", "60.0", "5 times")),
        3: ("10 times for 100.0$", lambda: buy_membership("Full Plan", "Pay-As-You-Go", "100.0", "10 times")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Full Plan - Pay-As-You-Go Membership", full_payg_menu)

def view_gym_short():
    gym_short_menu = {
        1: ("1 month for 12.0$", lambda: buy_membership("Gym Plan", "Short-Term", "12.0", "1 month")),
        2: ("3 months for 30.0$", lambda: buy_membership("Gym Plan", "Short-Term", "30.0", "3 months")),
        3: ("6 months for 50.0$", lambda: buy_membership("Gym Plan", "Short-Term", "50.0", "6 months")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Gym Plan - Short-Term Membership", gym_short_menu)

def view_gym_long():
    gym_long_menu = {
        1: ("1 year for 70.0$", lambda: buy_membership("Gym Plan", "Long-Term", "70.0", "1 year")),
        2: ("2 years for 130.0$", lambda: buy_membership("Gym Plan", "Long-Term", "130.0", "2 years")),
        3: ("5 years for 300.0$", lambda: buy_membership("Gym Plan", "Long-Term", "300.0", "5 years")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Gym Plan - Long-Term Membership", gym_long_menu)

def view_gym_payg():
    gym_payg_menu = {
        1: ("1 time for 18.0$", lambda: buy_membership("Gym Plan", "Pay-As-You-Go", "18.0", "1 time")),
        2: ("5 times for 80.0$", lambda: buy_membership("Gym Plan", "Pay-As-You-Go", "80.0", "5 times")),
        3: ("10 times for 150.0$", lambda: buy_membership("Gym Plan", "Pay-As-You-Go", "150.0", "10 times")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Gym Plan - Pay-As-You-Go Membership", gym_payg_menu)

def view_class_short():
    class_short_menu = {
        1: ("1 month for 12.0$", lambda: buy_membership("Class Plan", "Short-Term", "12.0", "1 month")),
        2: ("3 months for 30.0$", lambda: buy_membership("Class Plan", "Short-Term", "30.0", "3 months")),
        3: ("6 months for 60.0$", lambda: buy_membership("Class Plan", "Short-Term", "60.0", "6 months")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Class Plan - Short-Term Membership", class_short_menu)

def view_class_long():
    class_long_menu = {
        1: ("1 year for 50.0$", lambda: buy_membership("Class Plan", "Long-Term", "50.0", "1 year")),
        2: ("2 years for 90.0$", lambda: buy_membership("Class Plan", "Long-Term", "90.0", "2 years")),
        3: ("5 years for 200.0$", lambda: buy_membership("Class Plan", "Long-Term", "200.0", "5 years")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Class Plan - Long-Term Membership", class_long_menu)

def view_class_payg():
    class_payg_menu = {
        1: ("1 time for 12.0$", lambda: buy_membership("Class Plan", "Pay-As-You-Go", "12.0", "1 time")),
        2: ("5 times for 50.0$", lambda: buy_membership("Class Plan", "Pay-As-You-Go", "50.0", "5 times")),
        3: ("10 times for 90.0$", lambda: buy_membership("Class Plan", "Pay-As-You-Go", "90.0", "10 times")),
        4: ("Go Back", view_memberships),
    }
    display_menu("Class Plan - Pay-As-You-Go Membership", class_payg_menu)

def view_full_plan():
    full_plan_menu = {
        1: ("Short-Term", view_full_short),
        2: ("Long-Term", view_full_long),
        3: ("Pay-As-You-Go", view_full_payg),
    }
    display_menu("Full Plan Membership", full_plan_menu)

def view_gym_plan():
    gym_plan_menu = {
        1: ("Short-Term", view_gym_short),
        2: ("Long-Term", view_gym_long),
        3: ("Pay-As-You-Go", view_gym_payg),
    }
    display_menu("Gym Plan Membership", gym_plan_menu)

def view_class_plan():
    class_plan_menu = {
        1: ("Short-Term", view_class_short),
        2: ("Long-Term", view_class_long),
        3: ("Pay-As-You-Go", view_class_payg),
    }
    display_menu("Class Plan Membership", class_plan_menu)


def view_memberships_menu():
    global user
    membership_menu = {
        1: ("View All Membership Plans", view_memberships),
        2: ("View Membership Info", print_membership_info),
        3: ("View Your Current Membership Plan", view_current_membership_plan),
        4: ("Go back", lambda: display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu()))  # Same as requested
    }
    display_menu("Membership Menu", membership_menu)

def print_membership_info():
    membership_info = {
        "Class Plan": ("Offers access to all classes such as Yoga,                          Spinning, CrossFit, etc.", view_memberships_menu),
        "Gym Plan": ("Provides access only to the gym with all                            machines and equipment.", view_memberships_menu),
        "Full Plan": ("Gives access to both the gym and all available             classes.", view_memberships_menu),
        "Guest Trial: ": ("A free 1-week trial offering full access                  to both the gym and all classes for new users.", view_memberships_menu),
        "Short-Term Membership": ("Temporary access for 1 month,                                        3 months, etc.", view_memberships_menu),
        "Long-Term Membership": ("Extended access for 1 year, 2 years,                          or more.", view_memberships_menu),
        "Pay-as-You-Go": ("Pay for individual sessions or packages                             like 5 or 10 sessions.", view_memberships_menu),
        0: ("Press 0 to go back to the memberships menu", view_memberships_menu) 
    }
    display_menu("Membership Information", membership_info)

def display_workout_program(workouts):
    menu_options = {}
    for i, workout in enumerate(workouts, 1):
        # Replace '-' with a newline followed by '-' for better formatting
        formatted_description = workout.program_description.replace("-", "\n-").strip()
        menu_options[i] = (
            f"{workout.program_name}\n{formatted_description}",
            view_virtual_workout_programs
        )
    menu_options[len(menu_options) - 1] = ("Go back", view_virtual_workout_programs)
    display_menu("Workout Program Details", menu_options)


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
    time.sleep(1)
    input("Press any key to continue... ")
    display_menu(f"{(user.username).capitalize()}'s City Gym Hub", correct_main_menu())


# Menus
start_screen = {
    1: ("Sign Up", sign_up),
    2: ("Sign In", sign_in),
    3: ("Exit", None),
}


memberships_info = {
        1: ("The Basic Plan provides access to the main gym hall "
            "and all equipment and machines there.", None),
        2: ("The Premium Plan provides the same amenities as "
            "the Basic Plan while also giving you acces to "
            "our many classes we have, for example, CrossFit, "
            "Yoga and Pilates. The Premium Plan also gives you access "
            "to our spa area with a sauna, a cold tub and a hot tub.", None),
        3: ("Go back.", view_memberships)
        }



user_main_menu = {
    1: ("Memberships", view_memberships_menu),
    2: ("View Virtual Workout Programs", view_virtual_workout_programs),
    3: ("Track Workout History and Progress", lambda: track_workout_history_and_progress(user)),
    4: ("View and Book Classes", view_classes),
    5: ("Exit", None),
}


trainer_main_menu = {
    1: ("Memberships", view_memberships_menu),
    2: ("View Virtual Workout Programs", view_virtual_workout_programs),
    3: ("Track Workout History and Progress", lambda: track_workout_history_and_progress(user)),
    4: ("View and Book Classes", view_classes),
    5: ("Create Class", create_class), 
    6: ("Exit", None),
}

def main():
    """Main function to display the initial menu."""
    display_menu("City Gym Hub", start_screen)


if __name__ == "__main__":
    main()
