def group_anagrams(strings):
    anagrams = {}
    for string in strings:
        hash_value = my_hash_fun(string)
        if hash_value not in anagrams:
            anagrams[hash_value] = []
        anagrams[hash_value].append(string)
    
    result = []
    for key, anagram_lists in anagrams.items():
        result.append(anagram_lists)
    return result 
            
    
    
def my_hash_fun(string):
    hash_value = 0
    size = 7
    ord_multiple = 23
    for c in string:
        hash_value = (hash_value + ord(c)*23)
    hash_value = hash_value % 7
    return hash_value
    




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""