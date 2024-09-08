#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
        # Add the price of items to the total
        self.total += price * quantity
        # Keep track of each item, adding it 'quantity' number of times to the items list
        self.items.extend([title] * quantity)
        # Store the amount of the last transaction to allow for voiding
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            # Calculate discount and update total
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Print the updated total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract the last transaction amount from the total
        self.total -= self.last_transaction_amount
        # If all transactions are voided, ensure the total does not become negative
        if self.total < 0:
            self.total = 0.0

