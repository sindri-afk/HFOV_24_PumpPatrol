from BuyMembership import buy_application
import os
import sys
from prettytable import PrettyTable
import json

FILE_PATH = "/Users/sindribjarkason/Desktop/HFOV_24_PumpPatrol/MembershipPlan/membershipDB.json"

def main():
    is_true = True
    while is_true:

        # print(logo)
        print("1. Buy Membership\n2. View Memberships\n3. View Current Membership\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system('clear')
            plan = buy_application.main()
            main()
            is_true = False
        elif choice == "2":
            os.system('clear')
            table = PrettyTable()
            table.field_names = ["Membership Type", "Plan", "Price"]

            # Add rows to the table
            table.add_row(["Short Term", "One Month", "$170"])
            table.add_row(["Short Term", "Three Months", "$450"])
            table.add_row(["Short Term", "Six Months", "$800"])

            table.add_row(["Long Term", "One Year", "$1000"])
            table.add_row(["Long Term", "Two Years", "$1900"])
            table.add_row(["Long Term", "Three Years", "$2700"])

            table.add_row(["Pay As You Go", "Fee Upon Entry", "$15"])
            table.add_row(["Pay As You Go", "One Class Entrance", "$40"])
            print(table)
            print("1. Exit\n2. Main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                os.system('clear')
                sys.exit()
            elif choice == "2":
                os.system('clear')
                main()
            is_true = False

        elif choice == "3":
            os.system('clear')
            try:
                with open(FILE_PATH, 'r') as file:
                    data = json.load(file)
                    print(data)
                    print("1. Exit\n2. Main Menu")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        os.system('clear')
                        sys.exit()
                    elif choice == "2":
                        os.system('clear')
                        main()
            except Exception as e:
                print(f"Error reading file: {e}")

            is_true = False

        elif choice == "4":
            print("Exiting...")
            os.system('clear')
            sys.exit()
        else:
            continue
        if plan is not None:
            return plan

def write_json_file(file_path, data):
    try: 
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print("Data written to file.")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__=="__main__":
    os.system('clear')
    
    plan = main()
    if plan is not None:
        write_json_file(FILE_PATH, plan)

            
        
