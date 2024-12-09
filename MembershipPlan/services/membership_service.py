import json

class MembershipService:
    def __init__(self):
        self.membership_file = "MembershipPlan/data/membership.json"  # Make sure the file path is correct

    def load_memberships(self):
        """Load memberships from the JSON file."""
        try:
            with open(self.membership_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Membership file not found. Creating a new one at {self.membership_file}.")
            return []  # Return an empty list if the file doesn't exist
        except json.JSONDecodeError:
            print(f"Error decoding JSON in the membership file.")
            return []  # Return an empty list if JSON is invalid
        except Exception as e:
            print(f"Unexpected error loading memberships: {e}")
            return []

    def save_memberships(self, memberships):
        """Save the membership list to the JSON file."""
        try:
            with open(self.membership_file, "w") as f:
                json.dump(memberships, f, indent=4)
            print("Membership data successfully saved.")
        except Exception as e:
            print(f"Error saving memberships: {e}")

    def get_user_membership(self, username):
        """Retrieve the membership of a user by username."""
        memberships = self.load_memberships()
        user_membership = next((m for m in memberships if m["username"] == username), None)

        if user_membership:
            print(f"Your current membership plan: {user_membership['plan_name']} - {user_membership['type_name']} - ${user_membership['price']} for {user_membership['duration']}.")
            return user_membership
        else:
            print(f"You have not purchased a membership plan yet!")
            return None

    def buy_membership(self, username, plan_name, type_name, price, duration):
        """Buy or upgrade a membership for a user."""
        memberships = self.load_memberships()

        # Check if the user already has a membership
        existing_membership = next((m for m in memberships if m['username'] == username), None)

        # Enforce "Guest Trial" rule
        if plan_name == "Guest Trial":
            if existing_membership:
                print("Error: Guest Trial is only available to new users who have not purchased any membership.")
                return
            else:
                print(f"{username} is eligible for the Guest Trial.")

        if existing_membership:
            print(f"{username} already has a membership. Upgrading...")
            # Update the existing membership details
            existing_membership['plan_name'] = plan_name
            existing_membership['type_name'] = type_name
            existing_membership['price'] = price
            existing_membership['duration'] = duration
        else:
            print(f"{username} is purchasing a new membership.")
            # Add a new membership for the user
            memberships.append({
                "plan_name": plan_name,
                "type_name": type_name,
                "price": price,
                "duration": duration,
                "username": username
            })

        # Save the updated memberships
        self.save_memberships(memberships)
        print(f"Membership successfully updated: {plan_name} - ${price} for {duration}.")
