# main.py

from project_manager import ProductManager
from product import Product
from cart import Cart
import random


def main():
    manager = ProductManager()

    manager.add_product(Product("TV", 700, 20))
    manager.add_product(Product("iPhone", 1100, 70))
    manager.add_product(Product("Laptop", 1000, 30))

    print("Available Products:")
    manager.display_products()

    total_value = manager.total_value()
    print(f"\nTotal Inventory Value: ${total_value}")

    cart = Cart()

    products = manager.products
    for _ in range(3):
        product = random.choice(products)  
        max_quantity = min(product.quantity, 3)
        if max_quantity > 0:
            quantity = random.randint(1, max_quantity)  
            cart.add_to_cart(product, quantity)


    cart.display_cart()

    cart_total = cart.calculate_total()
    print(f"\nTotal Cart Value: ${cart_total:.2f}")



if __name__ == "__main__":
    main()
