from models.classes import Yoga, Cardio, Crossfit
from services.schedule_services import ScheduleService
from services.time_table import TimeTable
import os

    

def main():
    tt = TimeTable()
    tt.draw_table()
    sched = ScheduleService()
    sched.choose_class()
    sched.class_details()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()