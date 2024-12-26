# syntax
with open ("c:/Users/HP/Desktop/python programs/files/test3.txt","r") as f: #auto close file
    data=f.read()
    print(data)

with open ("c:/Users/HP/Desktop/python programs/files/test3.txt","w") as f: #auto close file
    f.write(" himagain ")
    print(f)
