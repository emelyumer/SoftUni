def even_odd(*args):
    even_list = []
    odd_list = []
    for el in args:
        if el == "even":
            return even_list
        elif el == "odd":
            return odd_list
        elif el % 2 == 0:
            even_list.append(el)
        else:
            odd_list.append(el)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))