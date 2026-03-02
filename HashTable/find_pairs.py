def find_pairs_bf(a1, a2, target):
    res_pairs = []
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i]+a2[j] == target:
                res_pairs.append((a1[i], a2[j]))
    return res_pairs

def find_pairs(a1, a2, target):
    res_pairs = []
    a2_hash = {}
    for i in range(len(a2)):
        a2_hash[a2[i]] = i
    for i in range(len(a1)):
        if (target-a1[i]) in a2_hash:
            res_pairs.append((a1[i], target-a1[i]))
    return res_pairs




arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 12, 2, 3, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)
