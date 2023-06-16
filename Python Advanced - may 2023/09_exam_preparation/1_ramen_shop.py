from collections import deque
bowl_list = deque(int(x) for x in input().split(", "))
customer_list = deque(int(x) for x in input().split(", "))

while bowl_list and customer_list:
    bowl = bowl_list.pop()
    customer = customer_list.popleft()
    if bowl == customer:
        continue
    elif bowl > customer:
        bowl -= customer
        bowl_list.append(bowl)
    elif bowl < customer:
        customer -= bowl
        customer_list.appendleft(customer)

if not customer_list:
    print("Great job! You served all the customers.")
    if bowl_list:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowl_list)}")
elif not bowl_list:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customer_list)}")



