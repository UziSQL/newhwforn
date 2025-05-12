def find_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))

print(find_union([1, 2, 3, 4], [3, 4, 5, 6])) # [1, 2, 3, 4, 5, 6]