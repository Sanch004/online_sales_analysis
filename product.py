class Product :
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        print(f"Product: {self.name}, Price: {self.price}, "
              f"Quantity: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
