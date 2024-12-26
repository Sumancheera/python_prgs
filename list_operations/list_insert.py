#insert the element at a given index
list=[1,2,3,4,5]
list2=[None]*(len(list)+1)
for i in range(len(list2)-1):
    list2[i]=list[i] #//transfering elements
print(list2)
pos=int(input("enter where you want to insert: "))
i=len(list2)-1
while i>pos-1:
    list2[i]=list[i-1] #shifting elements
    i-=1
list2[pos-1]=int(input("enter element u want to insert: "))
print(list2)

#using loops
list=[1,2,3,4,5]
list2=[0]*(len(list)+1)
index=int(input("enter the index val:")) #2
val=int(input("enter val:"))
j=0
for i in range(len(list2)): #starts from 0 and lst val dont include
    if(i==index):
        list2[i]=val    #i=0;1;2;3;4;5
    else:                #j=0;1;2;3;4
        list2[i]=list[j]
        j+=1
list=list2
print(list)
