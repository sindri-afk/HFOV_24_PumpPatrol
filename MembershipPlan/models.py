
class ShortTerm:
    def __init__(self):
        self.payment = int

    def one_month(self):
        self.payment = 170
        return self.payment

    def three_month(self):
        self.payment = 450
        return self.payment

    def six_month(self):
        self.payment = 800
        return self.payment

class LongTerm:
    def __init__(self):
        self.payment = int

    def one_year(self):
        self.payment = 1000
        return self.payment

    def two_year(self):
        self.payment = 1900
        return self.payment

    def three_year(self):
        self.payment = 2700
        return self.payment


class PayAsYouGo:
    def pay_as_you_go_gym(self):
        return "$15 per entry"
    def pay_as_you_go_class(self):
        return "$40 per class"


