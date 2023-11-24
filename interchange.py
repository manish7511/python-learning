# list=[2,3,4,5,6]
# temp=0

# for i in list:
#     temp=list[0]
#     list[0]=list[-1]
#     list[-1]=temp

# print(list)

#  2nd approach

# list=[2,3,4,5,6]
# list[0],list[-1]=list[-1],list[0]
# print(list)

#   3rd approach

list=[1,2,3,4,5,6]
get=list[-1],list[0]
list[0],list[-1]=get
print(list)