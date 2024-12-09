import sys
import os

class TimeTableMenuOptions:
    def __init__(self):
        self.timetable_options()
        
    def timetable_options(self):
        print("1. Choose class(1-10)")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.inspect_class_options()
        elif choice == "2":
            print("Goodbye!")
            sys.exit()
    
    def inspect_class_options(self):
        print("1. Book class")
        print("2. Inspect")
        print("3. Return to timetable")
        print("4. Exit")
        choice = input("Enter choice: ")
        return choice

    def __type_of_class(self):
        if self.timetable_options == "1" or self.timetable_options == "4" or self.timetable_options == "7" or self.timetable_options == "10":
            return "Yoga"
        elif self.timetable_options == "2" or self.timetable_options == "5" or self.timetable_options == "8":
            return "CrossFit"
        elif self.timetable_options == "3" or self.timetable_options == "6" or self.timetable_options == "9":
            return "Cardio"
        else:
            return "Invalid class choice"

    def __inspect_class_options(self):
        try:
            if self.inspect_class_options() == "1":
                print(f"{__type_of_class} Class booked!.")
            elif self.inspect_class_options() == "2":
                if __type_of_class == "Yoga":
                    yoga = Yoga()
                    return yoga.get_class_info()
                elif __type_of_class == "CrossFit":
                    crossfit = Crossfit()
                    return crossfit.get_class_info()
                elif __type_of_class == "Cardio":
                    cardio = Cardio()
                    return cardio.get_class_info()
                else:
                    return "Invalid class id"
            elif self.inspect_class_options() == "3":
                from ttmain import view_time_table
                print("Returning to timetable")
                view_time_table()

            elif self.inspect_class_options() == "4":
                print("Goodbye!")
                sys.exit()
        except ValueError:
            return "Invalid class id"


class ClassInspectionMenuOptions:

    def class_inspection_options(self):
        print("1. Book class")
        print("2. Return to timetable")
        print("3. Exit")
        choice = input("Enter choice: ")
        return choice