def count_frequency(my_list: list, element: int) -> int:
    count = 0
    for num in my_list:
        if num == element:
            count += 1
    return count

print(count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3)) # 2
