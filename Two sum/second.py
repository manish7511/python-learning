def two_sum(nums, target):
    # Create a dictionary to store the indices of numbers
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]

        
        num_indices[num] = i
    return None


nums = [2, 7, 11, 15]
target = 18
result = two_sum(nums, target)
print(result)
