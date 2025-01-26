from numpy import*
#we can convert the Any 2d-array to matrix for matrix fun,methods
#we can create our own matrix by giving vals.
arr=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
m=matrix(arr) #we use matrix instead of 2d-array, because of a few features.
print(m)
print("diagonal is: ",diagonal(m))
print(m.min())
print(m.max)


#we use matrix instead of 2d-array, because of a few features.
#like, diagnal,min,max,
m1=matrix('1,2,3;3,4,5;5,6,7') #m1=matrix('"1","2";"3","4"') for to store strings [['1' '2']
# ['3' '4']]
print(m1)

m2=matrix('"a" "b" "c" ; "d" "e" "f"') # we can use <space> or (,) to separate.
print(m2)

#multiplication of 2 matrix in python is very easy because of matric() - class, 
# +,*./ all constructores are defined in matrix class.
multiply=m*m1; 
#multiply=m*m1
print(multiply)