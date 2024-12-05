from models.classes import Yoga, Cardio, Crossfit
from services.time_table import TimeTable as tt
from services.class_inspection import ClassInspection
from utils.workshed import Toolbelt

class ScheduleService:
    def __init__(self):
        self.tools = Toolbelt()
        self.tt = tt()
        self.class_chosen = None

    def choose_class(self):
        print("please enter the number of the class you want to inspect")
        print("press E to exit")
        choice = input("\nChoose class: ")
        if choice.lower() =="e":
            self.tools.back_to_main_menu()
        if not choice.isdigit() or 0 >= int(choice) <= 12:
            self.tools.clear()
            print("Try again")
            self.choose_class()
        else:
            self.class_chosen = choice
            return choice

    def class_details(self):
        self.tools.clear()
        if not 1 >= int(self.class_chosen) <= 11:
            self.tools.clear()
            print("Invalid input")
            print("Try again!")
            self.choose_class() 

        class_id = int(self.class_chosen)
        class_inspection = ClassInspection()
        class_type = class_inspection.get_class_details(class_id)

        print(f"The class you have chosen is: \n{self.tools.print_chosen_class_timetable(class_id)}")
        

        print("\n1. Book class\n2. Inspect Class\n3. Back to TimeTable\n4. Exit")
        choice = input("\nChoose option: ")
        if int(choice) == 1:
            self.tools.clear()
            print(class_type)
            print(f"{self.class_chosen} Class booked!")
            
            self.tools.back_to_main_menu()
            # á eftir að skrifa tímann á userinn
            
        elif int(choice) == 2:
            print(class_inspection.print_class_details(class_id))
            
        elif int(choice) == 3:
            self.choose_class()
        elif int(choice) == 4:
            return
        else:
            print("Invalid input")
            print("Try again!")
            self.class_details()
        


