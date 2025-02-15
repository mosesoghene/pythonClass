from estore.product import Product

class Item:
    def __init__(self, quantity: int, product: Product):
        self.quantity = quantity
        self.product = product