def multiply(*args):
    result = 1
    for el in args:
        result *= int(el)
    return result
print(multiply(5, 6, 7))