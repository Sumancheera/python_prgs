def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd    #returning multimple vals 

list=[2,4,1,5,5,6,7,8,9,1,90,45,23,76,87,34,23,45,67,89,90]
even,odd=count(list)
print(f"even : {even} and odd num: {odd}")