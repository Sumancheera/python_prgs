arr=[1,2,3,4,5,6]
for i in range(len(arr)//2):
    last=arr[len(arr)-1]
    for j in range(len(arr)-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=last
print(arr)