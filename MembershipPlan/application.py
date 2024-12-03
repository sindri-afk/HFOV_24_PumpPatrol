from models import LongTerm, ShortTerm, PayAsYouGo
from routes import MembershipRoutes
import sys
import os
from membership_plan_logo import Logo
def main():
    logo = Logo.membership_plan_logo()
    print(logo)
    membership = MembershipRoutes()
    user_id = None
    print("\nChoose a membership plan:")
    print("1. Short Term")
    print("2. Long Term")
    print("3. Pay As You Go")
    print("4. Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('clear')
        membership._short_term()
    elif choice == "2":
        os.system('clear')
        membership._long_term()
    elif choice == "3":
        os.system('clear')
        membership._pay_as_you_go()
    elif choice == "4":
        print("Exiting...")
        sys.exit()
    else:
        pass

if __name__=="__main__":
    main()