def print_list(list,index):
    if index==len(list):
        return
    print(list[index])
    print_list(list,index+1)

list=[1,2,3,4,5]
print_list(list,0)