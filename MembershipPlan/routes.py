from models import LongTerm, ShortTerm, PayAsYouGo
from membership_plan_logo import Logo
import sys
import os

class MembershipRoutes:
    def __init__(self):
        self.short_term = ShortTerm()
        self.long_term = LongTerm()
        self.pay_as_you_go = PayAsYouGo()
        self.choice = None
        self.id = None
        self.logo = Logo

    def _short_term(self):
        is_true = True
        while is_true:
            print(self.logo.membership_plan_logo())
            print("\nChoose a short term membership plan:")
            print("1. One month: $",self.short_term.one_month())
            print("2. Three month: $",self.short_term.three_month())
            print("3. Six month: $",self.short_term.six_month())
            print("4. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                os.system('clear')
                print("\nYou have chosen one month membership plan with payment of $"+str(self.short_term.one_month()))
                self.id = "ST - 1"
                is_true = False
            elif choice == "2":
                os.system('clear')
                print("\nYou have chosen three month membership plan with payment of $"+str(self.short_term.three_month()))
                self.id = "ST - 2"
                is_true = False
            elif choice == "3":
                os.system('clear')
                print("\nYou have chosen six month membership plan with payment of $"+str(self.short_term.six_month()))
                self.id = "ST - 3"
                is_true = False
            elif choice == "4":
                os.system('clear')
                print("Exiting...")
                sys.exit()
            else:
                continue

        if self.id is not None:
            return self.id


    def _long_term(self):
        is_true = True
        while is_true:
            print(self.logo.membership_plan_logo())
            print("\nChoose a long term membership plan:")
            print("1. One year: $",self.long_term.one_year())
            print("2. Two year: $",self.long_term.two_year())
            print("3. Three year: $",self.long_term.three_year())
            print("4. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                os.system('clear')
                print("\nYou have chosen one year membership plan with payment of $"+str(self.long_term.one_year()))
                self.id = "LT - 1"
                is_true = False
            elif choice == "2":
                os.system('clear')
                print("\nYou have chosen two year membership plan with payment of $"+str(self.long_term.two_year()))
                self.id = "LT - 2"
                is_true = False
            elif choice == "3":
                os.system('clear')
                print("\nYou have chosen three year membership plan with payment of $"+str(self.long_term.three_year()))
                self.id = "LT - 3"
                is_true = False
            elif choice == "4":
                os.system('clear')
                print("Exiting...")
                sys.exit()
            else:
                continue
        if self.id is not None:
            return self.id


    def _pay_as_you_go(self):
        is_true = True
        while is_true:
            print(self.logo.membership_plan_logo())
            print("\nChoose a pay as you go plan:")
            print("1. Pay as you go to gym: $",self.pay_as_you_go.pay_as_you_go_gym())
            print("2. Pay as you go to class: $",self.pay_as_you_go.pay_as_you_go_class())
            print("3. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                os.system('clear')
                print("\nYou have chosen pay as you go to gym with payment of $"+str(self.pay_as_you_go.pay_as_you_go_gym()))
                self.id = "PAYG - 1"
                is_true = False
            elif choice == "2":
                os.system('clear')
                print("\nYou have chosen pay as you go to class with payment of $"+str(self.pay_as_you_go.pay_as_you_go_class()))
                self.id = "PAYG - 2" 
                is_true = False
            elif choice == "3":
                os.system('clear')
                print("Exiting...")
                sys.exit()
            else: 
                continue
        if self.id is not None:
            return self.id

        

