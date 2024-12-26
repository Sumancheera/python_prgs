# list syntax #list is mutable
list=[1,2,3,"suman",4.5,"ak"]

marks=[98.5,98.4,99.3,99.9,100, 101]
print(len(marks))
print(marks)
print(marks[0]) #we can acces in this way
print(type(marks))

list[5]="akshayani"
print(list)

#slicing // same as string slicing
#list_name[starting_index:ending _index] and ending index not included
print(marks[0:5:2]) #o to 5 and interval 2( gap).
print(marks[:2])
print(marks[0:])
print("extra",marks[0:6]) # and also [0:len(marks)]
print(marks[:])
print(marks[-6:-1:2]) #negative indexing with interval

#  [2  3  4  5  6  7]
#  -6 -5 -4 -3 -2 -1  // negatice indexing
#   0  1  2  3  4  5  //positive index  '
print(marks[0])  #first index val
print(marks[-6]) #first index val #marks[-len(marks)]


