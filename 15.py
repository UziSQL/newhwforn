def find_intersection(list1: list, list2: list) -> list:
    return [num for num in list1 if num in list2]

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6])) # [3, 4]