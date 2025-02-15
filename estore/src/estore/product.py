from estore.productcategory import ProductCategory
class Product:
    def __init__(self, product_id: int, price: float, description: str, product_name: str, category: ProductCategory):
        self.product_id = product_id
        self.price = price
        self.description = description
        self.product_name = product_name
        self.category = category
        