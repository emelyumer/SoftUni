from collections import deque
materials_toys = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
gift_level = {150: ["Doll", 0], 250: ["Wooden train", 0], 300: ["Teddy bear", 0], 400: ["Bicycle", 0]}
# presents = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
no_presents = True

while materials_toys and magic_level and no_presents == True:
    material = materials_toys.pop()
    magic = magic_level.popleft()
    result = material * magic
    if material == 0 and magic == 0:
        continue
    elif material != 0 and magic == 0:
        materials_toys.append(material + 15)
    elif material ==0 and magic != 0:
        magic_level.appendleft(magic)
    elif result in gift_level.keys():
        gift_level[result][1] += 1
    elif result < 0:
        result = material + magic
        materials_toys.append(result)
    elif result not in gift_level.keys():
        materials_toys.append(material + 15)

    if gift_level[150][1] > 0 and gift_level[250][1] > 0:
        no_presents = False
    elif gift_level[300][1] > 0 and gift_level[400][1] > 0:
        no_presents = False
print("bravo")




