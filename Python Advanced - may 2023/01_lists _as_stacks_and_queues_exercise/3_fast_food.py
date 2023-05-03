from collections import deque
food_for_theday = int(input())
all_orders = deque([int(x) for x in input().split()])
print(max(all_orders))
enough_food = True
while len(all_orders) > 0:
    current_order = all_orders[0]
    if food_for_theday >= current_order:
        food_for_theday -= current_order
        all_orders.popleft()
    else:
        enough_food = False
        break
if enough_food:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(o) for o in all_orders)}")
