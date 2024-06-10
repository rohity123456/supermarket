 # main.py

from product.core import Product
from offer.core import Offer
from checkout.core import Checkout

def main():
    pricing_rules = {}
    
    while True:
        print("\nEnter product details:")
        name = input("Product name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        price = int(input(f"Price of {name}: ").strip())
        product = Product(name, price)
        
        add_offer = input(f"Add offer for {name}? (y/n): ").strip().lower()
        while add_offer == 'y':
            offer_qty = int(input(f"Offer quantity for {name}: ").strip())
            offer_price = int(input(f"Offer price for {name}: ").strip())
            product.add_offer(Offer(offer_qty, offer_price))
            add_offer = input(f"Add another offer for {name}? (y/n): ").strip().lower()
        
        pricing_rules[name] = product
    
    print("\nProduct Pricing for this week:")
    print(f"{'Item':<5}{'Unit Price':<12}{'Special Price'}")
    print('-' * 30)
    for name, product in pricing_rules.items():
        offers = ", ".join([f"{offer.quantity} for {offer.price}" for offer in product.offers])
        print(f"{name:<5}{product.price:<10}{offers}")
    
    checkout = Checkout(pricing_rules)
    print("\nEnter items for checkout (type 'done' when finished):")
    while True:
        item = input("Item: ").strip()
        if item.lower() == 'done':
            break
        checkout.scan(item)
    
    total_price = checkout.total()
    print(f"\nTotal Price: {total_price}")

if __name__ == "__main__":
    main()
