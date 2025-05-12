def find_index(my_list: list, element: int) -> int:
    for i in range(len(my_list)):
        if my_list[i] == element:
            return i

    return -1

print(find_index([1, 2, 3, 4, 5], 3)) # 2
print(find_index([1, 2, 3, 4, 5], 6)) # -1