#i) Global Variable:
#Definition: A global variable is declared outside any function, meaning it can be accessed from anywhere within the program, including other functions.
#Example: Code

global_count = 0  

def increment(): 
        global global_count  
        global_count += 1 
#In this example, global_count can be accessed and modified by any function in the program because it's declared globally. 

#ii) Local Variable:
#Definition: A local variable is declared inside a function, and its scope is limited to that specific function.
#Example: Code

def calculate_area(length, width):
        area = length * width  
        return area 
#Here, area is a local variable only accessible within the calculate_area function. 

#iii) Nonlocal Variable:
#Definition: A nonlocal variable is used when you need to access and modify a variable from an enclosing function (a function that contains the current function) within a nested function.
#Example: Code
def outer_function():
        count = 0
        def inner_function():
            nonlocal count  
            count += 1
            print(count) 
        inner_function() 
#In this example, the count variable is considered nonlocal within the inner_function, allowing it to modify the count defined in the outer_function.