rows = int(input())
matrix = [[col for col in input()] for row in range(rows)]
symbol = input()
position = None
for row_idx in range(rows):
    if position:
        break
    for col_idx in range(len(matrix[0])):
        if matrix[row_idx][col_idx] == symbol:
            position = (row_idx, col_idx)
            break
if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")
