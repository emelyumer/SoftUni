from collections import deque
kids = deque(input().split())
toss_potato_counter = int(input())
counter = 0
while len(kids) > 1:
    counter += 1
    if counter == toss_potato_counter:
        counter = 0
        print(f"Removed {kids.popleft()}")
    else:
        kids.append(kids.popleft())

print(f"Last is {kids[0]}")

