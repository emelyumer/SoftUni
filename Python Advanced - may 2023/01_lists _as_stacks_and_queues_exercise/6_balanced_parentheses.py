from collections import deque
all_parentheses = deque(input())
left_parentheses = deque()
all_combination = ["{}", "()", "[]"]
for par in all_parentheses:
    if par in "{[(":
        left_parentheses.append(par)
    elif not left_parentheses:
        print("NO")
        break
    else:
        if left_parentheses:
            if left_parentheses.pop() + par not in all_combination:
                print("NO")
                break
else:
    print("YES")