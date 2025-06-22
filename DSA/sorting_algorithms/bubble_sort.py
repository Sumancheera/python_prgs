#bobble sorting
# fixing las one first
# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]: # put < if you need desending
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
# nums=[5,3,8,6,7,2]
# sort(nums) # calling
# print(nums)

#fixing first one first
def sorting(numss):
    for x in range(len(numss)):
        for y in range(x+1,len(numss)):
            if numss[x]>numss[y]: # put < if you need desending
                numss[x],numss[y]=numss[y],numss[x]
    print(numss)
numss=[72,2,9,6,71,8,9.5]
sorting(numss)
print(numss) # it will changes outside/original data also becase its list-mutable