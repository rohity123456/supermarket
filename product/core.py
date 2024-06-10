class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.offers = []

    def add_offer(self, offer):
        self.offers.append(offer)

    def calculate_price(self, quantity):
        total_price = 0
        remaining_qty = quantity

        # Sort offers by quantity in descending order to apply the best offers first
        sorted_offers = sorted(self.offers, key=lambda x: x.quantity, reverse=True)

        for offer in sorted_offers:
            if remaining_qty >= offer.quantity:
                num_offers = remaining_qty // offer.quantity
                total_price += num_offers * offer.price
                remaining_qty %= offer.quantity

        # Add the price for remaining items not covered by offers
        total_price += remaining_qty * self.price

        return total_price