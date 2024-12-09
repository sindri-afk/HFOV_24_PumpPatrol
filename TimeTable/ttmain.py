from timetable_controller import TimeTableController
from time_table_options import TimeTableMenuOptions as MenuOptions, ClassInspectionMenuOptions as ClassOptions


def view_time_table():
    tt_controller = TimeTableController()
    tt_controller.draw_table()
    time_menu = MenuOptions()
    time_menu.timetable_options()

if __name__ == "__main__":
    view_time_table()

