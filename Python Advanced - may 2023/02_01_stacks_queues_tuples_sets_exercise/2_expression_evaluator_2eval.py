from collections import deque
from math import floor
expression = deque(input().split())

idx = 0
while len(expression) > 1:
    element = expression[idx]
    if element in "+-/*":
        for _ in range(idx - 1):
            result = eval(f"{int(expression.popleft())} {element} {int(expression.popleft())}")
            expression.appendleft(result)

        del expression[1]
        idx = 1

    idx += 1


print(floor(int(expression[0])))