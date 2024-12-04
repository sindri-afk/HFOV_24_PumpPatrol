from ..repositories.membership_repository import MembershipRepository
from SignInUp.repositories.user_repository import UserRepository

class MembershipService:
    def __init__(self):
        self.repository = MembershipRepository()
        self.user_repository = UserRepository()

    def view_memberships(self):
        return self.repository.get_all_memberships()

    def buy_membership(self, user_id, plan_id):
        membership = self.repository.get_membership_by_id(plan_id)

        users = self.user_repository.load_users()
        user = next((u for u in users if u.user_id == user_id), None)

        user.membership_id = plan_id
        self.user_repository.save_users(users)

        print(f"You have successfully purchased the ${membership.price} {membership.name} for {membership.duration}!")

    
        