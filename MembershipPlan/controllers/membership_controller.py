from ..services.membership_service import MembershipService

class MembershipController:
    def __init__(self):
        self.service = MembershipService()

    def view_memberships(self):
        memberships = self.service.view_memberships()
        for membership in memberships:
            print(membership.to_dict())

    def buy_membership(self, plan_id):
        print(self.service.buy_membership(plan_id))