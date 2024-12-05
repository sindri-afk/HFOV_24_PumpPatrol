from models.classes import Yoga, Cardio, Crossfit
import sys
import os
from services.time_table import TimeTable
from utils.workshed import Toolbelt


class ClassInspection:
    def __init__(self):
        self.tools = Toolbelt()
    def get_class_details(self, class_id):
        if class_id == 1 or class_id == 4 or class_id == 7 or class_id == 10:
            return "Yoga"
        elif class_id == 2 or class_id == 5 or class_id == 8:
            return "Crossfit"
        elif class_id == 3 or class_id == 6 or class_id == 9:
            return "Cardio"
        else:
            print("Invalid input")
            sys.exit()
    
    def print_class_details(self, class_id):
        class_type = self.get_class_details(class_id)
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
            self.tools.back_to_time_table()  
    def class_details_options(self):
        self.tools.clear()
        self.tools.draw_table()

        print("1.Book class\n2. Back to TimeTable\n3. Exit")
        choice = input("\nChoose option: ")
        if int(choice) == 1:
            print("Class booked!")
            # á eftir að skrifa tímann á userinn
            sched_main()
        elif int(choice) == 2:
            self.tools.clear()
            self.tools.back_to_time_table()
        elif int(choice) == 3:
            print("Exiting....")
            sys.exit()


        return int(choice)