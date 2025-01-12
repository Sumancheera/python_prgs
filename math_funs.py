import math
#import math as m - #to use m.sqrt(n)
#if you want to use sqrt,pow diretly 
from math import sqrt,pow
print(pow(2,4)) # to use ditrctly without using math.xx
print(sqrt(12))
x=math.sqrt(25)
print(x )
print(math.pow(2,3))
print(3**2) #we can use ** to find power
print(math.floor(3.8)) 
print(math.ceil(2.3))
print(math.factorial(5))
print(math.pi)

#swap 2 variables 
a=1
b=2
a,b=b,a
print(a,b)
ch=eval(input("enter exp:")) # give any expression of math, 9-5=4
print(ch)       

#accepting multiple args, using argv
import sys
x=int(sys.argv[0])
y=int(sys.argv[1])
print(x+y)