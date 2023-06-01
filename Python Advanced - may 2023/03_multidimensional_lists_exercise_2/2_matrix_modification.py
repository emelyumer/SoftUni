rows = int(input())
matrix = [[int(col) for col in input().split()] for row in range(rows)]
command = input().split()
while command[0] != "END":
    action, index_row, index_col, number = [int(el) if el.isdigit() else el for el in command]
    if action == "Add" and index_row in range(rows) and index_col in range(rows):
        matrix[index_row][index_col] += number
    elif action == "Subtract" and index_row in range(rows) and index_col in range(rows):
        matrix[index_row][index_col] -= number
    else:
        print(f"Invalid coordinates")
    command = input().split()
print(*[' '. join([str(x) for x in row]) for row in matrix], sep="\n")
