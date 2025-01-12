####
####
####            #we need ro print this pattern
####
for i in range(4):
    for j in range(4):
        print("# ",end="")

    print() #for next line
####
###
##
#
print("then 2nd pattern")
for i in range(4):
    for j in range(4-i):
        print("# ",end="")

    print()
print("then 3rd pattern")
#
# #
# # #
# # # #
for i in range(4):
    for j in range(i+1):
        print("# ",end="")

    print()