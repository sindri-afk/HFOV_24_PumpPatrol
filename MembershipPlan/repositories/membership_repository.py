import json
from ..models.membership import Membership

class MembershipRepository:
    def __init__(self, file_path="MembershipPlan/data/membership.json"):
        self.file_path = file_path

    def get_all_memberships(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
            return [Membership.from_dict(item) for item in data]

    def get_membership_by_id(self, plan_id):
        memberships = self.get_all_memberships()
        print(memberships[1].name)
        for membership in memberships:
            if membership.plan_id == plan_id:
                return membership
        return None
 