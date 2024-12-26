# odd or even
num=int(input("enter the num:"))
if(num%2==0):
    print("even")
else:
    print("odd")

# greater of 4 numbers or 3
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
num4=int(input("enter the num4:"))
if(num1>num2 and num1>num3 and num1>num4):
    print("greater num:",num1)
elif(num2>num3 and num2>num4):
    print("greater num:",num2)
elif(num3>num4):
    print("greater num:",num3)
else:
    print("greater num:",num4)

#7 mul
num=int(input("enter the num:"))
if(num%7==0):
    print("7 multiple")
else:
    print("not 7 multiple")