from product import Product
from project_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("TV", 700, 10))
manager.add_product(Product("iPhone", 1200, 70))
manager.add_product(Product("Laptop", 900, 50))

print("Products: ")
manager.display_products()

print("Value of all products: ")
manager.total_value()

