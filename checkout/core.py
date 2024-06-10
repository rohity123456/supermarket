from product.core import Product

class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = {}

    def scan(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def total(self):
        total_price = 0
        for item, quantity in self.items.items():
            product = self.pricing_rules[item]
            total_price += product.calculate_price(quantity)
        return total_price