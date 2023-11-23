# list=[2,3,4,5,6,7]
# pos1,pos2=2,4
# list[pos1],list[pos2]=list[pos2],list[pos1]
# print(list)

 #   2nd approach

# list=[2,3,4,5,6]
# for i in list:
#     pos1,pos2=2,4
#     list[pos1],list[pos2]=list[pos2],list[pos1]
# print(list)

# 3rd approch
list=[2,3,4,5,6]
pos1,pos2=0,4

first_ele = list.pop(pos1)   
second_ele = list.pop(pos2-1)

list.insert(pos1, second_ele)  
list.insert(pos2, first_ele) 

print(list)


