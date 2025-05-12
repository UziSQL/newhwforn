def find_mode(my_list: list) -> int:
    frequency = {}
    for num in my_list:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]

    return modes[0]

print(find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3])) # 2