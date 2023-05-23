from collections import deque
bees = deque(int(x) for x in input().split())
nectar_s = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

honey = 0

while bees and nectar_s:
    bee = bees.popleft()
    nectar = nectar_s.pop()
    if bee < nectar:
        honey += abs(eval(f"{bee} {symbols.popleft()} {nectar}"))
    elif bee > nectar:
        bees.appendleft(bee)
print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar_s:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_s)}")