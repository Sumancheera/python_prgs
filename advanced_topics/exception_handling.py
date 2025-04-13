#syntax errors= compile time error , logical errors- correct logic or output= gives output but not correct
# run time errors - made by user wrong input or something wrong happened before starting ececution

a=6
b=2  # put 0
try: 
    print("opened")
    print(a/b)
    
except Exception as e:
    #you can perform any operation or run any script 
    print("opened")
    print(e, "or you cant enter zero")
finally :  # finally will execute any every case of try except
    print("closed")


print("prg ended")