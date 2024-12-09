import sys

def checkout(plan):
    print(f"You have selected the {plan} membership plan. ")
    confirm = input("Confirm plan (Y/N): ")
    if confirm.lower() == "y":
        print("Payment successful. Welcome to our gym!")
    elif confirm.lower() == "n":
        sys.exit()
        print("Payment cancelled. Goodbye.")
    else: 
        print("Invalid option. Try again.")
        checkout(plan)