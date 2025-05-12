def remove_all(my_list: list, element: int) -> list:
    return [num for num in my_list if num != element]

print(remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3)) # [1, 2, 4, 5, 1, 2]
