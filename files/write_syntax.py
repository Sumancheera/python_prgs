#writing the files 
f=open("c:/Users/HP/Desktop/python programs/files/test2.txt","w") # write mode
f.write("ill give that space. to shoe that i respect you.")
f.write("\n let me gues what you are doing")
f.write("\n trust me i wont compare")
f.close()

f=open("c:/Users/HP/Desktop/python programs/files/test2.txt","a+") #apend mode, writr at last without data loss
f.write("\n i forgot you say i wont scold you, no anger")
# data=f.read()
# print(data)
f.close()

f=open("c:/Users/HP/Desktop/python programs/files/test2.txt","r") #apend+ mode, writr at last without data loss, and we can print too
#f.write("\n now ill read")
data=f.read()
print(data)
f.close()


# write + #w+ same but, we will get data=f.read()
f=open("c:/Users/HP/Desktop/python programs/files/test3.txt","w+")
f.write(" see you ak")
f.write("starting")
f.close()

f=open("c:/Users/HP/Desktop/python programs/files/test3.txt","r")
data=f.read()
print(data)
f.close()


# in w+ and a+ you can still add data but if prints nothing, because one starting // one ending points and writes