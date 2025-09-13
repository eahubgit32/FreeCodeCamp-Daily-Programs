def find_missing_numbers(arr):
    if not arr:
        return []
    else:
        n = max(arr)
        full_array = set(range(1, n + 1))
        current_array = set(arr)
        missing = sorted(full_array - current_array)
        return(missing)

print(find_missing_numbers([1, 3, 5]))
