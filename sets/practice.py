#you are given sub for std . 1 clsroom needed for 1 subj, how many clsrooms needed by all std.?
set={"python","java","c++","python","javascript","java","python","java","c++","c"}
#to remove repeated val we have stored in set
# TO KNOW THE rooms num print its len
print(len(set))
set={"python","java","c++","python","javascript","java","python","java","c++","c",9,"9.0"} # to store 9,9.0
print(set)

#
set3={
    ("float",9.0),("int",9) #tuples in set
}
print(set3)

#wap input 3 std marks as val and subj names as keys
dict={}
x=int(input("enter math marks:"))
dict.update({"math":x})

x=int(input("enter physics marks:"))
dict.update({"physics":x})

x=int(input("enter chemistry marks:"))
dict.update({"chem":x})
print(dict)