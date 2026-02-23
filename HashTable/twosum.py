def two_sum(nums, total):
    inverse_dict = {}
    for i in range(len(nums)):
        if nums[i] not in inverse_dict:
            inverse_dict[nums[i]] = set()
        inverse_dict[nums[i]].add(i)
    
    for i in range(len(nums)):
        if (total - nums[i]) in inverse_dict:
            other_indices = inverse_dict[total-nums[i]] - {i}
            if other_indices:
                return [i, next(iter(other_indices))]
    return []


            
        
    
    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )
