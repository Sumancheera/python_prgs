#print("suman")
def increase_list_size(original_list, new_element):
    
    new_list_size = len(original_list) + 1 #5+1;
    new_list = [None] * new_list_size  #.? [none,none,none,none,none,"none"]
    print("ak")
    for i in range(len(original_list)): 
        new_list[i] = original_list[i] #i=0[1,none,none,none,none,"none"];#i=1[1,2,none,none,none,"none"];#i=2[1,2,3,none,none,"none"]
#i=3[1,2,3,4,none,"none"];#i=4[1,2,3,4,5,"none"].

    new_list[-1] = new_element  #.? [1,2,3,4,5,"6"].
    return new_list
#print("2nd print")
original_list=[1,2,3,4,5]
#print("hi")
new_list=increase_list_size(original_list,6)
print(new_list)

