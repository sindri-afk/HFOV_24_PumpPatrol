class Membership:
    def __init__(self, plan_id, name, price, duration):
        self.plan_id = plan_id
        self.name = name
        self.price = price
        self.duration = duration

    def to_dict(self):
        return {
            "plan_id": self.plan_id,
            "name": self.name,
            "price": self.price,
            "duration": self.duration,
        }

    @staticmethod
    def from_dict(data):
        return Membership(data["plan_id"], data["name"], data["price"], data["duration"])