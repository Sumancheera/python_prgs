from numpy import*  # it imports, math operations, logs,sin,cos, etc...
#numpy - numerical python
arr1=array([9,2,2,3,4])
arr1=arr1+5 # adds 5 to each element 
print(arr1)

#adding 2 arrays, add is diffrent from concatination.
arr2=array([3,4,5,6,7]) 
arr3=arr1+arr2             
print(arr3)

#vectorized operations
#sum, sin, cos, sqrt,
print(sum(arr1))
print(sin(arr1)) #sin,cos trignomatry
print(log(arr1))
print(min(arr1))
print(max(arr1))
print(unique(arr1))
print(sort(arr1))
print(sorted(arr1)) 

print(concatenate([arr1,arr2])) #print(concatinate(arr1,arr2)) TypeError: only integer scalar arrays can be converted to a scalar index

