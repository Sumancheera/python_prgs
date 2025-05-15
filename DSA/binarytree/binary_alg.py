# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(list,x):
    low,high,mid=0,len(list)-1,0
    while low<=high:
        mid=(high+low)//2
        # If x is greater, ignore left half
        if list[mid]==x:
            return mid
        #if x is smaller,ignore right side
        elif list[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1 # If we reach here, then the element was not present

list=[1,2,3,4,5,6,7,8,9,10]
x=7
result=binary_search(list,x)
if result !=-1:
    print("ele is present at:",str(result))
else:
    print("element is not found")

