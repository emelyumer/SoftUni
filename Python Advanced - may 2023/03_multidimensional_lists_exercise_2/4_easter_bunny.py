size = int(input())
field = []
bunny_position = []
best_direction = None
best_path = []
max_collected_eggs = 0


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    field.append(input().split())
    if "B" in field[row]:
        bunny_position = [row, field[row].index("B")]

for direction, position in directions.items():
    row, col = [
        bunny_position[0] + position[0],
        bunny_position[1] + position[1]
    ]
    path = []
    collected_eggs = 0
    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == 'X':
            break
        collected_eggs += int(field[row][col])
        path.append([row, col])
        row += position[0]
        col += position[1]
    if max_collected_eggs <= collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)
