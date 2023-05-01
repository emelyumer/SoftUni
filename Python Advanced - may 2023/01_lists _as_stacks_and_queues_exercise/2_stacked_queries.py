n_lines = int(input())
stack = []
for index in range(n_lines):
    query = input().split()
    if query[0] == "1":
        number = int(query[1])
        stack.append(number)
    elif query[0] == "2":
        if stack:
            stack.pop()
    elif query[0] == "3":
        print(max(stack))
    elif query[0] == "4":
        print(min(stack))
print(*stack[::-1], sep=", ")
