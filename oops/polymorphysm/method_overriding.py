
# 2)Run-Time Polymorphism:  It occurs when a subclass provides a specific implementation for a method already defined in its parent class, 
# commonly known as method overriding. show() in parent and child but executes in child
# becasue precendcey of child>parent.
class Dog:
    def sound(self):
        print("dog sound")  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overriding parent method
    
list=[Dog(),Labrador(),Beagle()] # Run-Time Polymorphism    
for i in list:
    i.sound() # Calls the appropriate method based on the object type
