#set is collection of unordered items, each elem in set must be unique & imutable
null_set= set()
nums={1,2,2,3,4} 
 #if set2={1,2,2,3,4} then {1,2,3,4} repeated will be removed 
# in set , str,tuple, int, float, bool - data types allowed , set ele should be hashable.
# list and dictionary is not allowed
print(nums)
print(type(nums))

#set.add(element)
#nums.add([5,6]) #TypeError: unhashable type: 'list'
nums.add(5)
print(nums)
#set.remove(element)
nums.remove(2)
print(nums)

#set.clear() #empties the set
nums.clear()
print(nums)

#set.pop # removes an randon value
set={"suman","ak",1,2,3,4,99.9}
print(set.pop())
print(set)

#set1.union(set2) # set1={1,2,3} set2={2,3,4} output: {1,2,3,4}
set1={1,2,3} 
set2={2,3,4}
print(set1.union(set2)) #it just forms the commom val not do changes in the origial set1, set2
print(set1.intersection(set2)) 

#Yes, a set in Python is mutable. This means you can add or remove elements from it after it is created.
#However, there's a catch: While the set itself can be modified, the elements within the set must be of an immutable type. 
# This means you cannot add lists or dictionaries to a set, but you can add strings, numbers, or tuples.