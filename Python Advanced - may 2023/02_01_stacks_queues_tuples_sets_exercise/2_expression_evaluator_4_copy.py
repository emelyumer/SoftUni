from collections import deque
data = input().split()
numbers = deque()
operators = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a // b,
}

for ch in data:
    if ch in "-+/*":
        while len(numbers) > 1:
            left = numbers.popleft()
            right = numbers.popleft()
            result = operators[ch](left, right)
            numbers.appendleft(result)

    else:
        numbers.append(int(ch))
print(numbers.popleft())