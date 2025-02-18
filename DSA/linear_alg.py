#python prg for linear search using iterative approach
def linear_search(arr,target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
    return -1        

arr=[1,2,3,4,5,6,7,8,9,10]
target=2

result=linear_search(arr,target)

if result !=-1:
    print(f"ele found at:{result}")
else:
    print("ele not found in the arr")

#Python Program for Linear Search Recursive Approach
def linear_search_recursive(list,target,index=0):
    if index==len(list):
        return -2
    if list[index]==target:
        return index
    return linear_search_recursive(list,target,index+1)
list=[10,20,30,40,50]
target=30
result=linear_search_recursive(list,target)
if result !=-1:
    print(f"element {target} found at",result)
else:
    print(f"element {target} not found in the list")