rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(col) for col in input().split(", ")] for r in range(rows)]
sum_cube = 0
for row_idx in range(rows-1):
    for col_idx in range(cols -1):
        current_cube_sum = matrix[row_idx][col_idx] + matrix[row_idx][col_idx + 1]\
                           + matrix[row_idx + 1][col_idx] + matrix[row_idx + 1][col_idx + 1]
        if current_cube_sum > sum_cube:
            sum_cube = current_cube_sum
            result = f"{matrix[row_idx][col_idx]} {matrix[row_idx][col_idx + 1]}\n{matrix[row_idx + 1][col_idx]} {matrix[row_idx + 1][col_idx + 1]}"
print(result)
print(sum_cube)
