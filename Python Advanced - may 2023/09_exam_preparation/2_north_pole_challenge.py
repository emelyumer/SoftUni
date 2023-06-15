# https://judge.softuni.org/Contests/Practice/Index/3306#1

def move(way):
    check_pos = [y_pos[0] + directions[way][0], y_pos[1] + directions[way][1]]
    if 0 <= check_pos[0] < rows and 0 <= check_pos[1] < cols:
        return check_pos

    elif not 0 <= check_pos[0] < rows:
        if check_pos[0] < 0:
            check_pos[0] = rows - 1
        elif check_pos[0] > rows - 1:
            check_pos[0] = 0
        return check_pos

    elif not 0 <= check_pos[1] < cols:
        if check_pos[1] < 0:
            check_pos[1] = cols - 1
        elif check_pos[1] > cols - 1:
            check_pos[1] = 0
        return check_pos


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


rows, cols = [int(x) for x in  input().split(", ")]
matrix = [input().split() for r in range(rows)]
y_pos = []
d_count = 0
g_count = 0
c_count = 0
items = 0

for r in range(len(matrix)):
    if "Y" in matrix[r]:
        y_pos = [r, matrix[r].index("Y")]
        matrix[y_pos[0]][y_pos[1]] = "x"
    if "D" in matrix[r]:
        items += matrix[r].count("D")
    if "G" in matrix[r]:
        items += matrix[r].count("G")
    if "C" in matrix[r]:
        items += matrix[r].count("C")


command = input().split("-")
while command[0] != "End" and items:
    times = int(command[1])
    for index in range(times):
        matrix[y_pos[0]][y_pos[1]] = "x"
        y_pos = move(command[0])
        if matrix[y_pos[0]][y_pos[1]] == "D":
            items -= 1
            d_count += 1
        elif matrix[y_pos[0]][y_pos[1]] == "G":
            items -= 1
            g_count += 1
        elif matrix[y_pos[0]][y_pos[1]] == "C":
            items -= 1
            c_count += 1
        matrix[y_pos[0]][y_pos[1]] = "Y"
        if not items:
            break


    if not items:
        break
    command = input().split("-")


if not items:
    print("Merry Christmas!")
print(f"You've collected:\n- {d_count} Christmas decorations\n- {g_count} Gifts\n- {c_count} Cookies")
print(*[' '.join(row) for row in matrix], sep="\n")





