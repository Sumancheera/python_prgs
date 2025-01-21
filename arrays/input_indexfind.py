from array import *
arr=array('i',[]) #empty array
n=int(input("enter the len:"))
for i in range(n):
    arr.append(i)
print(arr)
val=int(input("enter val:"))
j=0
for i in range(len(arr)):
    if i==val:
        print("the val is at:",j,"index")
        break
    j+=1
print(arr.index(val))


