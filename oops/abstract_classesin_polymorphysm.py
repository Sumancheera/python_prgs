#What is the role of abstract base classes in polymorphism?
#Abstract base classes (ABCs) define a common interface for a group of subclasses. 
# They cannot be instantiated themselves and require subclasses to provide implementations for their abstract methods. 
# ABCs ensure that derived classes adhere to a specific protocol, thus supporting polymorphism.

#Example:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):    
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
# Output:
# Bark
# Meow