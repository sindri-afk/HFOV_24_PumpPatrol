from BuyMembership.models import LongTerm, ShortTerm, PayAsYouGo
from BuyMembership.routes import MembershipRoutes
import sys
import os
import main as root_main


def main():
    membership = MembershipRoutes()
    membership_id = None
    print("Choose a membership plan:")
    print("1. Short Term")
    print("2. Long Term")
    print("3. Pay As You Go")
    print("4. Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('clear')
        membership_id = membership._short_term()


    elif choice == "2":
        os.system('clear')
        membership_id = membership._long_term()


    elif choice == "3":
        os.system('clear')
        membership_id = membership._pay_as_you_go()

    elif choice == "4":
        print("Exiting...")
        sys.exit()
    else:
        pass
    if membership_id is not None:
        return membership_id


# if __name__=="__main__":
#     os.system('clear')
#     main()

    