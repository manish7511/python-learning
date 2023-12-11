def twosum(number,target):
    for i in range(0,len(number)):
        for j in range(i+1,len(number)):
            if number[i] + number[j]==target:
               
                
               return number[i],number[j]
            




number=[1,5,7,-1]
target=8
a=twosum(number,target)
print(a)
