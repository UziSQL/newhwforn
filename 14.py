def rotate_right(my_list: list, k: int) -> list:
    k = k % len(my_list) if my_list else 0
    return my_list[-k:] + my_list[:-k] if k != 0 else my_list

print(rotate_right([1, 2, 3, 4, 5], 2)) # [4, 5, 1, 2, 3]