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