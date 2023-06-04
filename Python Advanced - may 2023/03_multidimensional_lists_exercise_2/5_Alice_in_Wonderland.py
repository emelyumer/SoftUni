def movement(way):
    alice_row = alice_position[0] + directions[way][0]
    alice_col = alice_position[1] + directions[way][1]
    if 0 <= alice_row < size and 0 <= alice_col <= size:
        return [alice_row, alice_col]
    return None


size = int(input())
matrix = []
alice_position = []
tea_counter = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[alice_position[0]][alice_position[1]] = "*"

while tea_counter < 10:
    command = input()
    alice_position = movement(command)
    if not movement:
        break
    position = matrix[alice_position[0]][alice_position[1]]
    matrix[alice_position[0]][alice_position[1]] = "*"
    if position == "R":
        break
    if position.isdigit():
        tea_counter += int(position)

if tea_counter < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in matrix], sep="\n")