from prettytable import PrettyTable

class TimeTable:
    def __init__(self):
        self.pt = PrettyTable()
    
    def draw_table(self):
        self.pt.field_names = ["Time", "Class", "Duration"]
        classes = [
            ("1. 06:30 - 07:30", "Yoga", "60 minutes"),
            ("2. 07:30 - 08:30", "CrossFit", "60 minutes"),
            ("3. 08:30 - 09:30", "Cardio", "60 minutes"),
            ("4. 09:30 - 10:30", "Yoga", "60 minutes"),
            ("5. 10:30 - 11:30", "CrossFit", "60 minutes"),
            ("6. 11:30 - 12:30", "Cardio", "60 minutes"),
            ("7. 12:30 - 13:30", "Yoga", "60 minutes"),
            ("8. 13:30 - 14:30", "CrossFit", "60 minutes"),
            ("9. 14:30 - 15:30", "Cardio", "60 minutes"),
            ("10. 15:30 - 16:30", "Yoga", "60 minutes")
        ]

        for time, class_name, duration in classes:
            self.pt.add_row([time, class_name, duration])
        print(self.pt)
    
