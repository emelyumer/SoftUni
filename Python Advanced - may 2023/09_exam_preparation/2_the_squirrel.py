# https://judge.softuni.org/Contests/Practice/Index/3893#1

def move(way):
    check_pos = [s_pos[0] + directions[way][0], s_pos[1] + directions[way][1]]
    if 0 <= check_pos[0] < size and 0 <= check_pos[1] < size:
        return check_pos
    return None


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_hazelnuts = 0
size = int(input())
commands = input().split(", ")
s_pos = []
matrix = []

for rr in range(size):
    matrix.append([])
    matrix[rr].extend(input())

for row in range(size):
    if "s" in matrix[row]:
        s_pos = [row, matrix[row].index("s")]

for command in commands:
    next_pos = move(command)
    if not next_pos:
        print("The squirrel is out of the field.")
        break
    s_pos = next_pos
    if matrix[s_pos[0]][s_pos[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if matrix[s_pos[0]][s_pos[1]] == "h":
        matrix[s_pos[0]][s_pos[1]] = "*"
        collected_hazelnuts += 1
        if collected_hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
else:
    if collected_hazelnuts < 3:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
