from address import Address
from creditcard import CreditCard

class Billing:
    def __init__(self, address: Address, credit_card: CreditCard, receiver_name: str, receiver_phone: str):
        self.address = address
        self.credit_card = credit_card
        self.receiver_name = receiver_name
        self.receiver_phone = receiver_phone