# test_checkout.py

import unittest
from product.core import Product
from offer.core import Offer
from checkout.core import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        pricing_rules = {
            'A': Product('A', 50),
            'B': Product('B', 30),
            'C': Product('C', 20),
            'D': Product('D', 15),
        }
        pricing_rules['A'].add_offer(Offer(3, 130))
        pricing_rules['B'].add_offer(Offer(2, 45))
        self.checkout = Checkout(pricing_rules)

    def test_empty_basket(self):
        self.assertEqual(self.checkout.total(), 0)

    def test_single_item(self):
        self.checkout.scan('A')
        self.assertEqual(self.checkout.total(), 50)

    def test_multiple_items_no_discount(self):
        self.checkout.scan('A')
        self.checkout.scan('B')
        self.assertEqual(self.checkout.total(), 80)

    def test_discount_applied(self):
        self.checkout.scan('A')
        self.checkout.scan('A')
        self.checkout.scan('A')
        self.assertEqual(self.checkout.total(), 130)

    def test_mixed_items(self):
        self.checkout.scan('A')
        self.checkout.scan('B')
        self.checkout.scan('A')
        self.checkout.scan('A')
        self.checkout.scan('B')
        self.assertEqual(self.checkout.total(), 175)

if __name__ == '__main__':
    unittest.main()
