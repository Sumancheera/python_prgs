from numpy import *    #Data processing size:32-bit,64-bit,  #refer to the architecture of a computer's processor, where the number indicates how large a chunk of data it can handle at once

arr=array([
    [1,2,3,4,5,6],
    [4,5,6,7,8,9]
])
print(arr)
print(arr.dtype) #attribute
print(arr.ndim)  # gives dimention
print(arr.shape)# 2 rows and coloums, exp (2,3) in tuple
print(arr.size)  # total elements count

#multi to single dimentional
arr2=arr.flatten()
print(arr2)

# single to multi dimentional.
arr3=arr2.reshape(3,2,2) #((alanti sets malli 2or3),(evi 2 sets),(1d-array lo 2 elements))
print(arr3)
print(arr3.ndim)

arr4=arr2.reshape(2,2,3) # (3d-array lo enni sets of 2d-arrays undali,2d-array lo enni array rows undali, 1d-array lo enni elements undali).
print(arr4)
print(arr4.ndim)

arr4=arr2.reshape(3,2,2) 
print(arr4)
print(arr4.ndim)

arr4=arr2.reshape(3,4,1) # 3[[[]]] unte 3D anthey
print(arr4)
print(arr4.ndim)

#(3d-array lo enni sets of 2d-arrays undali,2d-array lo enni array rows undali, 1d-array lo enni elements undali).





