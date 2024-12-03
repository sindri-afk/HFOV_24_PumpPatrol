from BuyMembership.models import LongTerm, ShortTerm, PayAsYouGo

import sys
import os
class MembershipRoutes:
    def __init__(self):
        self.short_term = ShortTerm()
        self.long_term = LongTerm()
        self.pay_as_you_go = PayAsYouGo()
        self.choice = None
        self.id = None


    def _short_term(self):
        is_true = True
        while is_true:
            print("Choose a short term membership plan:")
            print("1. One month: $",self.short_term.one_month())
            print("2. Three month: $",self.short_term.three_month())
            print("3. Six month: $",self.short_term.six_month())
            print("4. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                os.system('clear')
                print("You have chosen one month membership plan with payment of $"+str(self.short_term.one_month()))
                self.id = "Short term one month contract at $170"
                is_true = False
            elif choice == "2":
                os.system('clear')
                print("You have chosen three month membership plan with payment of $"+str(self.short_term.three_month()))
                self.id = "Short term three month contract at $450"
                is_true = False
            elif choice == "3":
                os.system('clear')
                print("You have chosen six month membership plan with payment of $"+str(self.short_term.six_month()))
                self.id = "Short term six month contract at $800"
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
            print("Choose a long term membership plan:")
            print("1. One year: $",self.long_term.one_year())
            print("2. Two year: $",self.long_term.two_year())
            print("3. Three year: $",self.long_term.three_year())
            print("4. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                os.system('clear')
                print("You have chosen one year membership plan with payment of $"+str(self.long_term.one_year()))
                self.id = "Long term one year contract at $1000"
                is_true = False
            elif choice == "2":
                os.system('clear')
                print("You have chosen two year membership plan with payment of $"+str(self.long_term.two_year()))
                self.id = "Long term two year contract at $1900"
                is_true = False
            elif choice == "3":
                os.system('clear')
                print("You have chosen three year membership plan with payment of $"+str(self.long_term.three_year()))
                self.id = "Long term three year contract at $2700"
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
            print("Choose a pay as you go plan:")
            print("1. Pay as you go to gym: $",self.pay_as_you_go.pay_as_you_go_gym())
            print("2. Pay as you go to class: $",self.pay_as_you_go.pay_as_you_go_class())
            print("3. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                os.system('clear')
                print("You have chosen pay as you go to gym with payment of $"+str(self.pay_as_you_go.pay_as_you_go_gym()))
                self.id = "Pay as you go to gym - $15"

                is_true = False
            elif choice == "2":
                os.system('clear')
                print("You have chosen pay as you go to class with payment of $"+str(self.pay_as_you_go.pay_as_you_go_class()))
                self.id = "Pay as you go to class - $40" 
                is_true = False
            elif choice == "3":
                os.system('clear')
                print("Exiting...")
                sys.exit()
            else: 
                continue
        if self.id is not None:
            return self.id

        

