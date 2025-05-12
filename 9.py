def is_sorted(my_list: list) -> bool:
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i - 1]:
            return False

    return True

print(is_sorted([1, 2, 3, 4, 5])) # True
print(is_sorted([1, 3, 2, 4, 5])) # False