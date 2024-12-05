from ..services.membership_service import MembershipService

class MembershipController:
    def __init__(self):
        self.service = MembershipService()

    def view_memberships(self):
        memberships = self.service.view_memberships()
        for membership in memberships:
            print(membership.to_dict())

    def buy_membership(self, user_id, plan_id):
        result = self.service.buy_membership(user_id, plan_id)