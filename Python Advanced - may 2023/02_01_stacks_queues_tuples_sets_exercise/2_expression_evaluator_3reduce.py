from functools import reduce
from math import floor
string_expression = input().split()
idx = 0
functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, string_expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, string_expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, string_expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, string_expression[:i]))
}

while len(string_expression) > 1:
    element = string_expression[idx]
    if element in "*/+-":
        # string_expression[0] е защото получената стойност от функцията ще заеме нулевата позиция на листа
        string_expression[0] = functions[element](idx)
        # понеже в горната фунция работим с копие на string_expression, след изпълнението й трябва да премахнем ненужните стойности
        [string_expression.pop(1) for i in range(idx)]
        idx = 1
    idx += 1

print(floor(int(string_expression[0])))