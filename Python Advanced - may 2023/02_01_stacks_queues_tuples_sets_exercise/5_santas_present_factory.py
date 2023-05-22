from collections import deque
materials_toys = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
gift_level = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents = {"Bicycle":0, "Doll":0, "Wooden train":0, "Teddy bear":0}
no_presents = True

while materials_toys and magic_level:
    material = materials_toys.pop()
    magic = magic_level.popleft()
    result = material * magic
    if material == 0 and magic == 0:
        continue
    elif material != 0 and magic == 0:
        materials_toys.append(material)
    elif material ==0 and magic != 0:
        magic_level.appendleft(magic)
    elif result in gift_level.keys():
        presents[gift_level[result]] += 1
    elif result < 0:
        result = material + magic
        materials_toys.append(result)
    elif result not in gift_level.keys():
        materials_toys.append(material + 15)

if presents["Bicycle"] > 0 and presents["Teddy bear"] > 0:
    no_presents = False
elif presents["Doll"] > 0 and presents["Wooden train"] > 0:
    no_presents = False

if no_presents:
    print("No presents this Christmas!")
else:
    print("The presents are crafted! Merry Christmas!")

if materials_toys:
    print(f"Materials left: {', '.join([str(x) for x in materials_toys][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in presents.items():
    if value > 0:
        print(f"{key}: {value}")
