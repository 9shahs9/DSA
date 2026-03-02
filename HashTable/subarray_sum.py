def subarray_sum(nums, target):
    sum_values = {}
    sum_values[0] = -1 
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if (current_sum - target) in sum_values:
            start_idx = sum_values[(current_sum-target)] + 1
            return [start_idx, i]
        sum_values[current_sum] = i 
    return []




nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
