## Unordered, mutable(changeble)
Dict={ 
    "name":"akshayani",    #key:value / "dont allow duplicate key names"
    "cgpa":9.98,
    "roll_num":1,
    "marks":(99,98,98.9), #list/ tuple anything we can add in values
    (1, 2, 3):["eng","telugu","hindi"],  #only tuples can add in keys.
    0:"null",
    0:True,
    1:False
    }
print(Dict.get(3,'not found'))   #imp syntax
print(type(Dict))
Dict["name"]="suman" # changing values
print(Dict["marks"]) #printing values using key name.

## Empty dictionary
null_dict={} 
# adding key: values to dictionary
#dict["key"]="value"/num.
null_dict["name"]="ak"
print(null_dict)

## Dictionar.methods() ##

#mydict.keys() # returns all the keys in dict
print(Dict.keys())
print(len(list(Dict.keys()))) #to convert dict keys into list list(method). ()not[]
print(list(Dict.keys()))
print(len(Dict.keys()))
print(len(Dict))

#Dict.values()
print(Dict.values())
print(list(Dict.values())) #list in list in dict-in-dict, possible, list,tuples in dict

#Dict.items()  # returns all (key,val)pairs as tuples
print(Dict.items())
#the ites or dict keys/vals/items we can convert to list/tuples.
pairs=list(Dict.items()) #items or vals/key convert to list and acces throgh [notation]
print(pairs[0])  #we can directly print.

#Dict.get("key") #return the key according to the value
print(Dict.get("name"))   #if error ir will return None val.
print(Dict["name"])  # error then after code wont work.

# Dict.update(newDict)  #insert the specified items to the dictionary.
# new_dict={"city":"hyderabad", "age":27}
# print(Dict.update(new_dict)) ## or add new pair
Dict.update({"city":"hyderabad"})
print(Dict["city"])

print(Dict.items())

#wap input 3 std marks as val and subj names as keys
dict={}
x=int(input("enter math marks:"))
dict.update({"math":x})

x=int(input("enter physics marks:"))
dict.update({"physics":x})

x=int(input("enter chemistry marks:"))
dict.update({"chem":x})
print(dict)

