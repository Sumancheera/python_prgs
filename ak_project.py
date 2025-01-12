class Product:
    def __init__(self, name, price_usd, quantity):
        self.name = name
        self.price_inr = price_usd * 83  # Convert from USD to INR
        self.quantity = quantity

    def get_total_price(self):
        return self.price_inr * self.quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ₹{self.price_inr:.2f}, Quantity: {self.quantity}, Total: ₹{self.get_total_price():.2f}"

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_cost(self):
        return sum(product.get_total_price() for product in self.products)

    def apply_discount(self, discount_percentage=None, fixed_discount=None):
        total_cost = self.calculate_total_cost()

        if discount_percentage:
            discount_amount = total_cost * (discount_percentage / 100)
        elif fixed_discount:
            discount_amount = fixed_discount
        else:
            discount_amount = 0

        discounted_total = total_cost - discount_amount
        return discounted_total, discount_amount

    def display_cart(self):
        for product in self.products:
            print(product)

def main():
    # Creating products (prices in USD, which will be converted to INR)
    product1 = Product("Laptop", 1000, 2)
    product2 = Product("Smartphone", 500, 3)
    product3 = Product("Headphones", 100, 5)
    product4 = Product("Tablet", 300, 1)
    product5 = Product("Smartwatch", 150, 4)
    product6 = Product("Keyboard", 50, 3)
    product7 = Product("Mouse", 25, 6)
    product8 = Product("Monitor", 250, 2)
    product9 = Product("Printer", 150, 1)
    product10 = Product("Charger", 20, 5)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to cart
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)
    cart.add_product(product4)
    cart.add_product(product5)
    cart.add_product(product6)
    cart.add_product(product7)
    cart.add_product(product8)
    cart.add_product(product9)
    cart.add_product(product10)

    # Display all products in the cart
    print("Shopping Cart Contents:")
    cart.display_cart()

    # Calculate the total cost without discount
    total_cost = cart.calculate_total_cost()
    print(f"\nTotal cost before discount: ₹{total_cost:.2f}")

    # Apply a discount (e.g., 15%)
    discount_percentage = 15
    discounted_total, discount_amount = cart.apply_discount(discount_percentage=discount_percentage)
    print(f"\nTotal cost after {discount_percentage}% discount: ₹{discounted_total:.2f}")
    print(f"Discount applied: ₹{discount_amount:.2f}")

    # Alternatively, apply a fixed discount (e.g., ₹1000 off)
    fixed_discount = 1000
    discounted_total_fixed, discount_amount_fixed = cart.apply_discount(fixed_discount=fixed_discount)
    print(f"\nTotal cost after ₹{fixed_discount} fixed discount: ₹{discounted_total_fixed:.2f}")
    print(f"Fixed discount applied: ₹{discount_amount_fixed:.2f}")

if __name__ == "__main__":
    main()
