class Circle:
    def __init__(self, radius,num):
        self._radius = radius
        self.num=num

    @property
    def radius(self):
        print("hello")
        return self._radius
    def justcall(self):
        print("calling as fun")

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value


# Create a Circle object
my_circle = Circle(5,2)  # Initialize radius to 5

# Access the radius (using the getter)
print("Initial radius:", my_circle.radius,my_circle.num) #one attibute,one method but using same syntax
print("fun call:",my_circle.justcall()) #here we need (), but not for radius fun
# Change the radius (using the setter)
my_circle.radius
print("New radius:", my_circle.radius) #calling method as attribute.

# Try to set an invalid radius
try:
    my_circle.radius = -2
except ValueError as e:
    print("Error:", e)

try:
    my_circle.radius = "abc"
except ValueError as e:
    print("Error:", e)