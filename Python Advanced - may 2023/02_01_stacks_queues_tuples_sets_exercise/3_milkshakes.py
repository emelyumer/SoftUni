from collections import deque
chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(y) for y in input().split(", "))
milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    last_choco = chocolates.pop()
    first_cup = cups_of_milk.popleft()

    if last_choco <= 0 and first_cup <= 0:
        continue
    elif last_choco <= 0 and first_cup > 0:
        cups_of_milk.appendleft(first_cup)
        continue
    elif last_choco > 0 and first_cup<=0:
        chocolates.append(last_choco)
        continue
    elif last_choco == first_cup:
        milkshakes += 1
    else:
        chocolates.append(last_choco - 5)
        cups_of_milk.append(first_cup)


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(z) for z in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(z) for z in cups_of_milk) or 'empty'}")