#Using lambda with filter()
#The filter() function in Python takes in a function and a list as arguments. 
# This offers an elegant way to filter out all the elements of a sequence “sequence”, 
# for which the function returns True.
n=[1,2,3,4,5,6]
#filter(func,iterable)
even=list(filter(lambda x:x%2==0,n))
print(even)
#even=filter(lambda x:x%2==0,n)
# for i in even:
#     print(i)

# Function to check if a number is even
def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)

# Convert filter object to a list
print(list(b))

##### Using lambda with map() #####
#The map() function in Python takes in a function and a list as an argument. 
# The function is called with a lambda function and a new list is returned 
# which contains all the lambda-modified items returned by that function for each item.
a=[1,2,3,4,5]
b=map(lambda x:x*2,a) #here only you can convert list
print(list(b))

##### Using lambda with reduce() ######
#The reduce() function in Python takes in a function and a list as an argument. 
#The function is called with a lambda function and an iterable and a new reduced result is returned. 
#This performs a repetitive operation over the pairs of the iterable. 
# The reduce() function belongs to the functools module. 
from functools import  reduce
a=[1,2,3,4,5,6,7,8,9,10]
b=reduce(lambda x,y:x+  y,a)
#b object is int,  we can directly print
print(b) 

# https://www.geeksforgeeks.org/python-map-function/