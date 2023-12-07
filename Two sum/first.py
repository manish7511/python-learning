def twosum(numbers,target):
    left,right=0,len(numbers)-1

    while left<right:
        current_sum=numbers[left]+numbers[right]

        if current_sum==target:
            return [numbers[left],numbers[right]]
        elif current_sum<target:
            left=left+1
        else:
            right=right-1
numbers=[3,2,4,5]
target=9
result=twosum(numbers,target)
print(result)

        