from models import LongTerm, ShortTerm, PayAsYouGo
import sys

class MembershipRoutes:
    def __init__(self):
        self.short_term = ShortTerm()
        self.long_term = LongTerm()
        self.pay_as_you_go = PayAsYouGo()
        self.choice = None

    def _short_term(self):
        is_true = True
        while is_true:
            print("\nChoose a short term membership plan:")
            print("1. One month: $",self.short_term.one_month())
            print("2. Three month: $",self.short_term.three_month())
            print("3. Six month: $",self.short_term.six_month())
            print("4. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                print("\nYou have chosen one month membership plan with payment of $"+str(self.short_term.one_month()))
                is_true = False
            elif choice == "2":
                print("\nYou have chosen three month membership plan with payment of $"+str(self.short_term.three_month()))
                is_true = False
            elif choice == "3":
                print("\nYou have chosen six month membership plan with payment of $"+str(self.short_term.six_month()))
                is_true = False
            elif choice == "4":
                print("Exiting...")
                sys.exit()
            else:
                continue


    def _long_term(self):
        is_true = True
        while is_true:
            print("\nChoose a long term membership plan:")
            print("1. One year: $",self.long_term.one_year())
            print("2. Two year: $",self.long_term.two_year())
            print("3. Three year: $",self.long_term.three_year())
            print("4. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                print("\nYou have chosen one year membership plan with payment of $"+str(self.long_term.one_year()))
                is_true = False
            elif choice == "2":
                print("\nYou have chosen two year membership plan with payment of $"+str(self.long_term.two_year()))
                is_true = False
            elif choice == "3":
                print("\nYou have chosen three year membership plan with payment of $"+str(self.long_term.three_year()))
                is_true = False
            elif choice == "4":
                print("Exiting...")
                sys.exit()
            else:
                continue


    def _pay_as_you_go(self):
        is_true = True
        while is_true:
                
            print("\nChoose a pay as you go plan:")
            print("1. Pay as you go to gym: $",self.pay_as_you_go.pay_as_you_go_gym())
            print("2. Pay as you go to class: $",self.pay_as_you_go.pay_as_you_go_class())
            print("3. Exit\n")
            choice = input("Enter your choice: ")
            # return choice
            if choice == "1":
                print("\nYou have chosen pay as you go to gym with payment of $"+str(self.pay_as_you_go.pay_as_you_go_gym()))
                is_true = False
            elif choice == "2":
                print("\nYou have chosen pay as you go to class with payment of $"+str(self.pay_as_you_go.pay_as_you_go_class())) 
                is_true = False
            elif choice == "3":
                print("Exiting...")
                sys.exit()
            else: 
                continue
        

