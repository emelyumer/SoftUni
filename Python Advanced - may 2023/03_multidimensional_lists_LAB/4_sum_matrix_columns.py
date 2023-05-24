row, col = [int(x) for x in input().split(", ")]
matrix = [[col for col in input().split()] for row in range(row)]

for index_col in range(col):
    sum_col_elements = 0
    for index_row in range(row):
        sum_col_elements += int(matrix[index_row][index_col])
    print(sum_col_elements)

