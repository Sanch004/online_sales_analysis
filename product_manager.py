from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.product_info()

    def total_value(self):
        value = 0
        for product in self.products:
            value += product.price * product.quantity
        return print(value)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
