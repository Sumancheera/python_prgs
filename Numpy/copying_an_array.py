from numpy import*
arr1=array([1,2,3,45,6])
arr2=array([3,4,5,6,7])
arr=arr1  # aliasing
print(arr,id(arr)) #variable name is diffrent 
print(arr1,id(arr1)) # butr smme address is pointing

#shallow copy. even if you craete a diffrent variablen still they are dependent on each other.
arr3=arr1.view()
arr4=arr1.copy() #deep_copy
arr1[0]=7
print(arr1,arr3)
print(id(arr1),id(arr3))

#deep copy- old_array.copy() #it will give diffrent and individual array
print(arr1,arr4)
print(id(arr1),id(arr4))



