from ..repositories.membership_repository import MembershipRepository

class MembershipService:
    def __init__(self):
        self.repository = MembershipRepository()

    def view_memberships(self):
        return self.repository.get_all_memberships()

    def buy_membership(self, plan_id):
        membership = self.repository.get_membership_by_id(plan_id)
        print(f"You have successfully purchased the {membership.price} {membership.name} for {membership.duration}!")

    
        