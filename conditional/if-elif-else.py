#trafic light exp
light=input("enter the colour:")

if(light=="red"):
    print("stop") #indentation insted of {}
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("wait")
else:
    print("light is off or broken")

#grades
marks=int(input("enter your marks:"))
if(marks>=90 and marks<=100):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
elif(marks>=60 and marks<70):
    grade="D"
else: 
    if(marks>100 or marks<=-1):
        grade="invalid marks"
    else:
        grade="fail"
print(grade)

#age #nested if
age=int(input("enter your age:"))
if(age>=18):
    print("adult")
    if(age>19 and age<40):
        print("middle age")
        if(age>=40 and age<60):
            print("senior adult")
            if(age>=60 and age<80):
                print("senior citizen")
