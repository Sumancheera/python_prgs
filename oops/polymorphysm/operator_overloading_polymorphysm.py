#operation overloading 
#using operators or Dunder functions
# a.__add__(b) / a.__sub__(b) / a.__mul__(b) / a.__truediv__(b) / a.__mod__(b)
#add/sub
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownum(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img    
        return Complex(newreal,newimg )
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img    
        return Complex(newreal,newimg )

num1=Complex(1,2)
num1.shownum()

num2=Complex(4,5)
num2.shownum()

#num3=num1.add(num2)
num3=num1+num2
num3.shownum()
num4=num2-num1
num4.shownum()

# Python program to show use of
# + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("Geeks"+"For") 

# Product two numbers
print(3 * 4)

# Repeat the String
print("Geeks"*4)