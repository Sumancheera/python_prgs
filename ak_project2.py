class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def apply_discount(self, discount_percentage):
        discount_amount = self.calculate_total() * (discount_percentage / 100)
        return self.calculate_total() - discount_amount

# Example usage
print("your items list and prices are:")
product1 = Product("Laptop", 80000)
print(product1.name,product1.price)
product2 = Product("Mouse", 500)
print(product2.name,product2.price)
product3 = Product("Keyboard", 1500)
print(product3.name,product3.price)
print()

cart = ShoppingCart()
cart.add_item(product1)
cart.add_item(product2)
cart.add_item(product3)

print("Total cost:", cart.calculate_total(), "₹")

discount_percentage = int(input("enter your discount %:"))  # 10% discount
discounted_total = cart.apply_discount(discount_percentage)
print("Discounted total:", discounted_total, "₹")