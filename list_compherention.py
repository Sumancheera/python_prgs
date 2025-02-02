list1=[a for a in range(0,10)]
print(list1)

list2=[a for a in list1 if a%2==0]  # list comperension with condition 
print(list2)

list3=[a*a for a in list2]
print(list3)

a = [1,2,3,4,5]
result = [val * 2 for val in a] #val *+-/ anything is possible
print(result)

#using append()
res=[]
for i in a:
    res.append(i+1)
print(res)

#nested loop coordinates filling
coordinates=[(x,y) for x in range(3) for y in range(3)]
print(coordinates)

#flttening a list of lists
# mat[0]=[1,2,3]
mat=[[1,2,3],[4,5,6],[7,8,9]]
res=[val for sumblist in mat for val in sumblist]
print(res)

#using zip()
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
res=[(x,y,z) for x,y,z in zip(a,b,c)]
print(res)

#using enumerate()