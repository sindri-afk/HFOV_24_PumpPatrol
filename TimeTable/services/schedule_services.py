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
        print("please enter the number of the class you want to inspect(1-10)")
        print("press E to exit")
        choice = input("\nChoose class: ")
        if choice.lower() == "e":
            print("Exiting....")
            self.tools.exit()
        try:
            if int(choice) < 1 or int(choice) > 10:
                self.tools.clear()
                print("Try again")
                self.choose_class()
            elif int(choice) > 0 and int(choice) < 11:
                self.tools.clear()
                self.class_chosen = choice
                return choice
            else:
                self.tools.clear()
                print("That is not an option...")
                self.tools.draw_table()
                self.choose_class()
        except ValueError:
            self.tools.clear()
            print("That is not an option...")
            self.tools.draw_table()
            self.choose_class()

    def class_details(self):
        if 0 >= int(self.class_chosen) or int(self.class_chosen) >= 12:
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
        try:
            if int(choice) == 1:
                self.tools.clear()
                print(f"{class_type} Class booked!\n")
                
                self.tools.back_to_time_table()
                # á eftir að skrifa tímann á userinn
                
            elif int(choice) == 2:
                if class_type == "Yoga":
                    self.tools.clear()
                    yoga = Yoga()
                    print(yoga.get_details())
                    self.class_details_options()
                    
                elif class_type == "Crossfit":
                    self.tools.clear()
                    crossfit = Crossfit()
                    print(crossfit.get_details())
                    self.class_details_options()
                elif class_type == "Cardio":
                    self.tools.clear()
                    cardio = Cardio()
                    print(cardio.get_details())
                    self.class_details_options()
                else:
                    self.tools.clear()
                    print("Invalid input\n Try again!")
                    self.class_details()

                
            elif int(choice) == 3:
                self.tools.clear()
                self.tools.back_to_time_table()
                self.choose_class()
            elif int(choice) == 4:
                self.tools.exit()
            else:
                print("Invalid input")
                print("Try again!")
                self.class_details()
        except ValueError:
            self.tools.clear()
            print("Invalid input")
            print("Try again!")
            self.class_details()    
    
    def class_details_options(self):
        print("1. Book class\n2. Back to TimeTable\n3. Exit")
        choice = input("\nChoose option: ")
        if int(choice) == 1:
            self.tools.clear()
            print("Class booked!")
            # á eftir að skrifa tímann á userinn
            self.tools.back_to_time_table()
        elif int(choice) == 2:
            self.tools.clear()
            self.tools.back_to_time_table()
        elif int(choice) == 3:
            print("Exiting....")
            sys.exit()
        else:
            print("Invalid input")
            print("Try again!")
            self.class_details_options()


