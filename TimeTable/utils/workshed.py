class Toolbelt:

    def back_to_time_table(self):
        from schedule_main import main as sched_main
        sched_main()
    def draw_table(self):
        from services.time_table import TimeTable
        tt = TimeTable()
        tt.draw_table()
    def clear(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    def exit(self):
        import sys
        sys.exit()
    def print_chosen_class_timetable(self, id):
        classes_sched_list = ["06:30 - 07:30: Yoga", 
        "07:30 - 08:30: CrossFit", 
        "08:30 - 09:30: Cardio", 
        "9:30 - 10:30: Yoga", 
        "10:30 - 11:30: CrossFit", 
        "11:30 - 12:30: Cardio", 
        "12:30 - 13:30: Yoga", 
        "13:30 - 14:30: CrossFit", 
        "14:30 - 15:30: Cardio", 
        "15:30 - 16:30: Yoga", 
        "16:30 - 17:00: CrossFit"]
        return classes_sched_list[id-1]

    
    