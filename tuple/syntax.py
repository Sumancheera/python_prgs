# tuple #immutable like strings, can not change
#tuple=(), tuple=1, // tuple="ak", // tuple="ak",1 // tuple=("ak",1)

marks=(99, 98, 97.5, 100, 101) #list2             #(a+b)
print(marks)
print(type(marks))

#you can only acces by array notation
print(marks[0])

# you can slice tuple too
print(marks[0:2])
# 0 to len, empty:empty, //strt:end:interva all are avalable

#tuple methods
tup=(2,1,3,1,1,4,5,1)
#idx=0,1,2,3
  #tup.index(element) will give index of 1st occarence
print(tup.index(1))
 #tup.count(element) # counts total occurences
print(tup.count(1))