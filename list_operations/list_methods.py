#list- methods
# 1) list.append(element)
marks=[98.5,98.4,99.3,99.9,100, 101]

marks.append(4) #adding element at last 
print(marks)

#2)sorting
marks.sort() #ascending order #none val returns we have to print list variable again
print(marks)
list=["mango", "banana", "apple"] #same with sorting of char also
list.sort()
print(list)

# 3)sort - dedcending order
marks.sort(reverse=True)
print(marks)

# 4)list.reverse() #reverse the list  [3,2,1]
rev=[3,2,1]
rev.reverse()
print(rev)

#5) insert in the lsit
# list.insert(index,element)
rev.insert(3,4)
print(rev)

#6) list.remove(1) exp: [1,2,3,4]
# remove 1st occurence of element
rev.remove(4)
print(rev)

#7) list.pop(index)
# remove element at index.
rev.pop(2)
print(rev)

#extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

list=[1,2,1,3,2,4,2,1,3]
print(list.index(4)) #index val of 1st occurence of that num/char/string/float
print(list.count(1)) #count of list val by giving that val