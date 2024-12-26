#default parameters:
# assigning a default value to parameters, which is used when no argument is paased. 
 
def cal_prod(a,b=1): # a=1,b=1// sum=1; 
    sum=a*b
    print(sum)
    return sum
cal_prod(1) #1st agrument goes to 1st parameter. 
