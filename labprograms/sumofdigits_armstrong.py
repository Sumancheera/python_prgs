n=int(input("enter the num up to 999:"))
# sum of digits
sum=0
# while n>0:
#     rem=n%10
#     sum+=rem
#     n=n//10
# print(sum)

#armstrong num
initial=n
while n>0:
    rem=n%10
    if n<=999:
        sum+=(rem*rem*rem)
    else:
        sum+=(rem*rem*rem*rem)
    n=n//10
if initial==sum:
    print("armstrong")
else:
    print("not armstrong" )