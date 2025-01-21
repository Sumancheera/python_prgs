list2="1#2#3#4"
arr=list(map(int,list2.split("#")))
#arr=list(map(int,input().split())) if nothing is mentioned in the split by defoult you can give - space- it will take as separeate item
print(arr)


def sumofarray(n,arr1):
    sum=0
    for i in arr1:
        sum=sum+i
    return sum

n=int(input("enter num of numbers you need"))
arr1=list(map(int,input("enter num and space, enter num space:").split()))
print(sumofarray(n,arr1))
print(arr1)