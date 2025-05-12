def remove_duplicates(my_list: list) -> list:
    a = set()
    b = []
    for i in my_list:
        if i not in a:
            b.append(i)
            a.add(i)

    return b

print(remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4])) # [1, 2, 3, 4, 5]