from collections import deque
from math import floor
string_expression = deque(input().split())
# print(string_expression)

idx = 0
while len(string_expression) > 1:
    element = string_expression[idx]
    if element == "*":
        for _ in range(idx -1):
            result = int(string_expression.popleft()) * int(string_expression.popleft())
            string_expression.appendleft(str(result))
    elif element == "+":
        for _ in range(idx -1):
            result = int(string_expression.popleft()) + int(string_expression.popleft())
            string_expression.appendleft(str(result))
    elif element == "-":
        for _ in range(idx -1):
            result = int(string_expression.popleft()) - int(string_expression.popleft())
            string_expression.appendleft(str(result))
    elif element == "/":
        for _ in range(idx -1):
            result = int(string_expression.popleft()) // int(string_expression.popleft())
            string_expression.appendleft(str(result))

    idx += 1
    if element in "+-/*":
        string_expression.remove(element)
        idx = 0


print(*string_expression)