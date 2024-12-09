import json

class MembershipService:
    def __init__(self):
        self.membership_file = "MembershipPlan/data/membership.json"  # Make sure the file path is correct

    def get_user_membership(self, username):
        try:
            # Load the existing membership data from the file
            with open(self.membership_file, "r") as f:
                memberships = json.load(f)
                
                # Filter memberships by username
                user_membership = next((m for m in memberships if m["username"] == username), None)
                
                if user_membership:
                    print(f"Your current membership plan: {user_membership['plan_name']} - ${user_membership['price']}, {user_membership['duration']}.")
                    return user_membership
                else:
                    print(f"You have not purchased a membership plan yet!")
                    return None
        except Exception as e:
            print(f"Error loading memberships: {e}")
            return None

    def is_not_membership(self, username):
        """Check if the user has no membership."""
        user_membership = self.get_user_membership(username)
        if user_membership is None:
            return True
        return False

    def buy_membership(self, username, plan_name, type_name, price, duration):
        try:
            with open(self.membership_file, "r") as f:
                memberships = json.load(f)

            # Check if the user already has a membership
            existing_membership = next((m for m in memberships if m['username'] == username), None)

            if existing_membership:
                print(f"{username} already has a membership. Upgrading...")
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

            # Save the updated membership list to the file
            with open(self.membership_file, "w") as f:
                json.dump(memberships, f, indent=4)
                
            print(f"Membership successfully updated: {plan_name} - ${price} for {duration}.")
        except Exception as e:
            print(f"Error purchasing membership: {e}")
