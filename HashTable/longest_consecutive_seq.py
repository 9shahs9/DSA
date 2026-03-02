def longest_consecutive_sequence(nums):
    sorted_list = sorted(nums)
    if len(nums) == 0:
        return 0
    curr_long = 1 
    max = 1
    for i in range(1,len(sorted_list)):
        if sorted_list[i] == sorted_list[i-1] + 1:
            curr_long +=1
        elif sorted_list[i] == sorted_list[i-1]:
            continue
        else:
            if curr_long > max:
                max = curr_long 
            curr_long = 1
    if curr_long > max:
        return curr_long 
    return max 
    

# ============================================
# Test Cases for Longest Consecutive Sequence
# ============================================

# Test Case 1: Basic unsorted array with consecutive sequence
assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4, "Test Case 1 Failed"
print("✓ Test Case 1 Passed: Basic unsorted array with consecutive sequence")

# Test Case 2: Empty array
assert longest_consecutive_sequence([]) == 0, "Test Case 2 Failed"
print("✓ Test Case 2 Passed: Empty array")

# Test Case 3: Single element
assert longest_consecutive_sequence([5]) == 1, "Test Case 3 Failed"
print("✓ Test Case 3 Passed: Single element")

# Test Case 4: Two consecutive elements
assert longest_consecutive_sequence([1, 2]) == 2, "Test Case 4 Failed"
print("✓ Test Case 4 Passed: Two consecutive elements")

# Test Case 5: Two non-consecutive elements
assert longest_consecutive_sequence([1, 3]) == 1, "Test Case 5 Failed"
print("✓ Test Case 5 Passed: Two non-consecutive elements")

# Test Case 6: All identical elements
assert longest_consecutive_sequence([5, 5, 5, 5]) == 1, "Test Case 6 Failed"
print("✓ Test Case 6 Passed: All identical elements")

# Test Case 7: Only negative numbers (consecutive)
assert longest_consecutive_sequence([-5, -3, -4, -2]) == 4, "Test Case 7 Failed"
print("✓ Test Case 7 Passed: Only negative numbers (consecutive)")

# Test Case 8: Mix of positive and negative numbers
assert longest_consecutive_sequence([-1, 0, 1, 2, 5, 6, 7]) == 4, "Test Case 8 Failed"
print("✓ Test Case 8 Passed: Mix of positive and negative numbers")

# Test Case 9: Array with duplicates
assert longest_consecutive_sequence([1, 2, 2, 3, 4, 4, 5]) == 5, "Test Case 9 Failed"
print("✓ Test Case 9 Passed: Array with duplicates")

# Test Case 10: Multiple gaps between sequences
assert longest_consecutive_sequence([1, 2, 3, 10, 11, 12, 20, 21]) == 3, "Test Case 10 Failed"
print("✓ Test Case 10 Passed: Multiple gaps between sequences")

# Test Case 11: Already sorted array
assert longest_consecutive_sequence([1, 2, 3, 4, 5]) == 5, "Test Case 11 Failed"
print("✓ Test Case 11 Passed: Already sorted array")

# Test Case 12: Reverse sorted array
assert longest_consecutive_sequence([5, 4, 3, 2, 1]) == 5, "Test Case 12 Failed"
print("✓ Test Case 12 Passed: Reverse sorted array")

# Test Case 13: Large numbers
assert longest_consecutive_sequence([1000000, 1000002, 1000001, 1000003]) == 4, "Test Case 13 Failed"
print("✓ Test Case 13 Passed: Large numbers")

# Test Case 14: Only negative numbers with gaps
assert longest_consecutive_sequence([-10, -8, -7, -5]) == 2, "Test Case 14 Failed"
print("✓ Test Case 14 Passed: Only negative numbers with gaps")

# Test Case 15: Zero in the middle of sequence
assert longest_consecutive_sequence([-2, -1, 0, 1, 2]) == 5, "Test Case 15 Failed"
print("✓ Test Case 15 Passed: Zero in the middle of sequence")

# Test Case 16: Multiple sequences of equal length
assert longest_consecutive_sequence([1, 2, 3, 10, 11, 12]) == 3, "Test Case 16 Failed"
print("✓ Test Case 16 Passed: Multiple sequences of equal length")

# Test Case 17: One long sequence with outliers
assert longest_consecutive_sequence([100, 1, 2, 3, 4, 5, 6, 7, 200]) == 7, "Test Case 17 Failed"
print("✓ Test Case 17 Passed: One long sequence with outliers")

# Test Case 18: Consecutive sequence starting from negative
assert longest_consecutive_sequence([-5, -4, -3, -2, -1, 0, 1]) == 7, "Test Case 18 Failed"
print("✓ Test Case 18 Passed: Consecutive sequence starting from negative")

# Test Case 19: Single negative number
assert longest_consecutive_sequence([-42]) == 1, "Test Case 19 Failed"
print("✓ Test Case 19 Passed: Single negative number")

# Test Case 20: No consecutive numbers (all gaps > 1)
assert longest_consecutive_sequence([1, 3, 5, 7, 9, 11]) == 1, "Test Case 20 Failed"
print("✓ Test Case 20 Passed: No consecutive numbers (all gaps > 1)")

print("\n" + "="*50)
print("All 20 test cases passed! ✓")
print("="*50)

