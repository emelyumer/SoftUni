def even_odd_filter(**kwargs):
    for type, num_list in kwargs.items():
        if type == "odd":
            kwargs[type] = [num for num in kwargs[type] if num % 2 != 0]
        elif type == "even":
            kwargs[type] = [num for num in kwargs[type] if num % 2 == 0]
    return dict(sorted(kwargs.items(), key=lambda item: -len(item[1])))


print(even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    ))
