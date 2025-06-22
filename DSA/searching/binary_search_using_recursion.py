# Python 3 program for recursive binary search.
def binary_search_rec(arr, low2, high2, x2):
    # Check base case
    if high2 >= low2:
        mid2 = (high2 + low2) // 2
        # If element is present at the middle itself
        if arr[mid2] == x2:
            return mid2
        elif arr[mid2]>x2:
            return binary_search_rec(arr,low2,mid2-1,x2)
        else:
            return binary_search_rec(arr,mid2+1,high2,x2)
    else:
        return -1
arr=[1,2,3,4,5,6,7,8]
x2=5
result2 = binary_search_rec(arr, 0, len(arr)-1, x2)
print(result2)
 
if result2 != -1:
    print("Element is present at index", str(result2))
else:
    print("Element is not present in array")