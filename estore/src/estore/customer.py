from estore.billing import Billing
from estore.user import User

class Customer(User):
    def __init__(self):
        super().__init__()
        self.shopping_cart: Item = []
        self.billing_information: Billing = Billing()