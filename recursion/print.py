# recursion is called as calling the fun it self again and again, like loops
# condition x base case

def printnum(n): #n=100 to 1
    if n==0:
        return # saying return and end the call stack, no need to return because this is print fun.
    print(n)
    printnum(n-1)

printnum(50)    

#call stack4 - return
#call stack3 - comes here
#call stack2 - then here
#call stack1 - finally here.
