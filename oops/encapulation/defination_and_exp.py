#Example of Encapsulation:
#Encapsulation in Python refers to the bundling of data with the methods that operate on that data. 
# It restricts direct access to some of the object’s components, which can prevent the accidental modification of data. 
# In Python, encapsulation is typically achieved by prefixing names of attributes or methods with a single underscore (weakly private) 
# or double underscore (strongly private) to suggest or enforce that they are meant to be private.


class Computer:
    def __init__(self):
        self.__max_price = 900  # Private attribute

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()

# Trying to directly access a private variable
# print(c.__max_price)  # This will raise an AttributeError

# Using a method to modify a private variable
c.set_max_price(1000)
c.sell()  # Output: Selling Price: 1000