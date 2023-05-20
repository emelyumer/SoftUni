from collections import deque
materials_toys = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
gift_level = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
no_presents = True

while materials_toys or magic_level or no_presents:
    material = materials_toys.pop()
    magic = magic_level.popleft()
    result = material * magic
    if result in gift_level.keys():
        presents

