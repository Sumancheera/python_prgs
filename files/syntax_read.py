#file to open and read/write then close 
f=open("c:/Users/HP/Desktop/python programs/files/suman.txt","r") #r or rt // readtext mode #txt is default
data=f.read(8) #reads only first 8 char
print(data)
data=f.read() #reads total data but excludes before readed 8 char, already read
print(data)
f.close

f=open("c:/Users/HP/Desktop/python programs/files/test.txt","r+") #r+ reading and writing no truncate.
data=f.readline()
print(data)
f.write("ak this me again")
data=f.readline() #reads one line at a time // reads first line// if we use same line agin it will reads 2nd.
print(data)
f.close
# if you want to print the same line then close the file and again exe the line 
