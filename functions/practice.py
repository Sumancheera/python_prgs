#In Python, the syntax for a lambda function is 
# lambda parameters: expression. 
# For example, x = lambda a, b : a + b 
# creates a lambda function that multiplies argument a with argument b and returns the result.

def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
n=int(input("enter the num:"))
even_odd(n)