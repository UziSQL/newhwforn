def find_difference(list1: list, list2: list) -> list:
    return [num for num in list1 if num not in list2]

print(find_difference([1, 2, 3, 4], [3, 4, 5, 6])) # [1, 2]