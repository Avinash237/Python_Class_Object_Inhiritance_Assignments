class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from cart.")
                return
        print(f"{product_name} not found in cart.")

    def display_cart(self):
        if not self.products:
            print("Your cart is empty.")
        else:
            print("Your Shopping Cart:")
            for product in self.products:
                product.display_product()

    def checkout(self):
        total_price = sum(product.price * product.quantity for product in self.products)
        print(f"Total amount to be paid: {total_price}")


# Example usage:
if __name__ == "__main__":
    # Creating some products
    product1 = Product("Shirt", 500, 2)
    product2 = Product("Jeans", 800, 1)
    product3 = Product("Shoes", 1200, 1)

    # Creating a shopping cart
    cart = ShoppingCart()

    # Adding products to the cart
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # Displaying the cart
    cart.display_cart()

    # Removing a product from the cart
    cart.remove_product("Shirt")

    # Displaying the cart after removal
    cart.display_cart()

    # Checking out
    cart.checkout()
