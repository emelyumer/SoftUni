def move(way):
    check_pos = [m_pos[0] + directions[way][0], m_pos[1] + directions[way][1]]
    if 0 <= check_pos[0] < rows and 0 <= check_pos[1] < cols:
        return check_pos
    return None


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


rows, cols = [int(x) for x in input().split(",")]
matrix = []
m_pos = []
cheese_count = 0

for row in range(rows):
    matrix.append([])
    matrix[row].extend(input())
    if "M" in matrix[row]:
        m_pos = [row, matrix[row].index("M")]
        matrix[m_pos[0]][m_pos[1]] = "*"
    if "C" in matrix[row]:
        cheese_count += matrix[row].count("C")

command = input()
if command == "danger":
    matrix[m_pos[0]][m_pos[1]] = "M"

while command != "danger":
    next_pos = move(command)
    if not next_pos:
        matrix[m_pos[0]][m_pos[1]] = "M"
        print("No more cheese for tonight!")
        break
    if matrix[next_pos[0]][next_pos[1]] == "@":
        command = input()
        if command == "danger":
            matrix[m_pos[0]][m_pos[1]] = "M"
        continue
    if matrix[next_pos[0]][next_pos[1]] == "T":
        m_pos = [next_pos[0], next_pos[1]]
        matrix[m_pos[0]][m_pos[1]] = "M"
        print("Mouse is trapped!")
        break
    if matrix[next_pos[0]][next_pos[1]] == "C":
        matrix[next_pos[0]][next_pos[1]] = "*"
        m_pos = [next_pos[0], next_pos[1]]
        cheese_count -= 1
        if cheese_count == 0:
            matrix[next_pos[0]][next_pos[1]] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    m_pos = [next_pos[0], next_pos[1]]
    command = input()
    if command == "danger":
        matrix[m_pos[0]][m_pos[1]] = "M"

else:
    if cheese_count > 0:
        print("Mouse will come back later!")


print(*[''.join(r) for r in matrix], sep="\n")




