#Abstraction or Data abstarction
#Partial Abstraction: The Dog class has both abstract (sound) and concrete (display_name) methods.
#Why Use It: Abstraction ensures consistency in derived classes by enforcing the implementation of abstract methods.
#Data Abstraction 
#Abstraction hides the internal implementation details while exposing only the necessary functionality. 
# It helps focus on “what to do” rather than “how to do it.”

#Types of Abstraction:
#Partial Abstraction: Abstract class contains both abstract and concrete methods.
#Full Abstraction: Abstract class contains only abstract methods (like interfaces).

from abc import ABC,abstractclassmethod
class Dog(ABC):
    def __init__(self,name):
        self.name=name

    @abstractclassmethod
    def sound(self):
        pass #abstract method, at least one should have

    # def display_names(self,): #concrete method
    #     print(f"dogs name:{self.name}")

class Labrador(Dog):
    def sound(self):
        print("labrador munugudu or woof")

class Beagle(Dog):
    def sound(self):
        print("beagle bark or kuyu kuyu")

list=[Labrador("puppy"),Beagle("suresh")]
for dogs in list:
    dogs.display_names()
    dogs.sound()


#Abstraction: Hiding complex implementation details and providing a simplified interface.

