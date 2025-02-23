from product import Product
from project_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("TV", 700, 20))
manager.add_product(Product("iPhone", 1100, 70))
manager.add_product(Product("Laptop", 1000, 30))


