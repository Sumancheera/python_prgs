from numpy import*
#from array import* TypeError: array() argument 1 must be a unicode character, not list ; line 6

# we can create arrays using
# array(), linspace(),logspace(), arnage(), zeros(), ones().
#array() - this is the first method and, its diffrent from arrays in array library(1d arrays)
arr=array([1,2,3,4,5],float) 
#arr=array([list elements],datatype_convertion/specify)
print(arr.dtype)
print(type(arr))
arr1=array(arr)
#array() in arrays v/s array() in numpy same but arguments changes.
print(arr1)
print(type(arr1))
array_name=array([4,5,6,7]) # #arr=array([list elements],optional)
print(array_name)

# arr=linspace(start,end,no_of_parts)
linespace_array=linspace(1,20,6) #by defoult its in float, end included.
print(linespace_array)

#arr=arange(first,last,steps) like range(), last smae excluded.
arange_array=arange(7,17,2) # it will give odd num, started with odd
print(arange_array) 

#arr=logspace(start,end,parts) # in between 10 pow start to 10 pow end. it will give n parts.
logspace_array=logspace(1,40,4) #[1.e+01 1.e+14 1.e+27 1.e+40]
print(logspace_array)


#arr=zeros(size/no of elements,optional(int/float)) # it will give all zeros
zeros_array=zeros(7)
print(zeros_array) 

#ones
ones_array=ones(8,int)
print(ones_array)