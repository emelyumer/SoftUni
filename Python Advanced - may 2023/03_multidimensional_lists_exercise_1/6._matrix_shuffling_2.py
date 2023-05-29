rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)
command, *list_el = [int(y) if y.isdigit() else y for y in input().split()]
while command != "END":
    if command != "swap" or len(list_el) != 4 or list_el[0] not in valid_rows or list_el[2] not in valid_rows or list_el[1] not in valid_cols or list_el[3] not in valid_cols:
        print("Invalid input!")
    else:
        row1, col1, row2, col2 = list_el
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        print(*[' '.join(r) for r in matrix], sep="\n")

    command, *list_el = [int(y) if y.isdigit() else y for y in input().split()]

