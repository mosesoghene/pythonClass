from cardtype import CardType

class CreditCard:
    def __init__(self,
                 card_number: str, cvv: int,
                 expiration_month: int, expiration_year: int,
                 name_on_card: str, card_type: CardType
                 ):
        self.card_number = card_number
        self.cvv = cvv
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.name_on_card = name_on_card
        self.card_type = card_type