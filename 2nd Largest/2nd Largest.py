def second_largest(arr):

    unique_numbers = list(set(arr))

    sorted_list = sorted(unique_numbers, reverse=True)

    if len(sorted_list) > 1:
        second_largest_number = sorted_list[1]
    else:
        second_largest_number = None 

    return second_largest_number

print(second_largest([2, 3, 4, 6, 6]))
