def array_diff(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return sorted(set1.symmetric_difference(set2))


print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
