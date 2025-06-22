# selection sort, we will select min or max first then writes the logic so selection sort
def selection_sort(arr):
    for i in range(len(arr)-1):
        minpos=i
        for j in range(i,len(arr)):
            if arr[minpos]>arr[j]:
                minpos=j
        arr[i],arr[minpos]=arr[minpos],arr[i]
        # print(arr)
    return arr
sorted=selection_sort(arr=[7,5,3,9,1,0,2])
print(sorted)