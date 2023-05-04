from collections import deque
all_parentheses = deque(input().split())
left_parentheses = deque()
for par in all_parentheses:
    if par in "{[(":
        left_parentheses.append(par)
    elif not left_parentheses:
        print("NO")
    else:
        if left_parentheses:
            if par + left_parentheses