from collections import deque

energy = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])
total_used_energy = 0
total_number_of_toys = 0
elf_counter = 0

while materials and energy:
    elf = energy.popleft()

    if elf < 5:
        continue

    box = materials.pop()
    elf_counter += 1

    if box > elf:
        elf *= 2
        energy.append(elf)
        materials.append(box)
    elif elf_counter % 15 == 0:
        if elf >= (box * 2):
            total_used_energy += (box * 2)
            elf -= (box * 2)
        else:
            materials.append(box)
            elf *= 2
        energy.append(elf)
    elif elf_counter % 3 == 0:
        if elf >= (box * 2):
            total_number_of_toys += 2
            total_used_energy += (box * 2)
            elf -= (box * 2)
            elf += 1
        else:
            materials.append(box)
            elf *= 2
        energy.append(elf)
    elif elf_counter % 5 == 0:
        total_used_energy += box
        elf -= box
        energy.append(elf)
    else:
        elf -= box
        elf += 1
        energy.append(elf)
        total_number_of_toys += 1
        total_used_energy += box

print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")
if energy:
    print(f"Elves left: {', '.join([str(e) for e in energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(y) for y in materials])}")




