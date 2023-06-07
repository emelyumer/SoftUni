from functools import reduce


def operate(symbol, *args):
    if symbol == "+":
        return reduce(lambda a, b: a + b, args)
    elif symbol == "-":
        return reduce(lambda a, b: a - b, args)
    elif symbol == "*":
        return reduce(lambda a, b: a * b, args)
    else:
        return reduce(lambda a, b: a / b, args)


print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))