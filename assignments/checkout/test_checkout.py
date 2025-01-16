from unittest import TestCase
from checkout import *


class TestCheckoutApp(TestCase):
    def test_that_function_add_product_to_exists(self):
        cart = []
        add_product_to(cart, "Parfait", 2, 2100)
    
    def test_that_product_is_added_to_cart(self):
        cart = []
        actual = add_product_to(cart, "Parfait", 2, 2100.0)
        expected = [{'product': "Parfait", 'quantity': 2, 'price': 2100.0}]
        self.assertEqual(actual, expected)
        


