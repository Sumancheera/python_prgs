# polymorphysm are 2 types
#1)Compile-Time Polymorphism:  It is commonly referred to as method or operator overloading.


# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    # def add(self,a,b):
    #     print("executed")  #it wont work fully in python
    #     return a+b
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()
    
calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments

#Method overloading refers to the ability to have multiple methods with the same name but different parameters within the same class. 
# Python does not support method overloading by default. However, we can achieve method overloading-like behavior by providing default values for parameters 
# or by using variable-length arguments.


#Example Simulating Method Overloading:
class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("Nothing to display")

obj = Example()
obj.display()
obj.display(10)
obj.display(10, 20)

# First product method.
# Takes two argument and print their
# product


def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)


# or by using variable-length arguments.
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4))