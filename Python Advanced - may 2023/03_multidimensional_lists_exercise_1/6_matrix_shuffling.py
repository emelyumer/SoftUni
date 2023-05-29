def check_valid_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


def swap_command(commands, indices):
    if check_valid_indices(indices) and commands == "swap" and len(indices) == 4:
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        print(*[' '.join(r) for r in matrix], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)
command, *list_el = [int(y) if y.isdigit() else y for y in input().split()]
while command != "END":
    swap_command(command, list_el)
    command, *list_el = [int(y) if y.isdigit() else y for y in input().split()]

