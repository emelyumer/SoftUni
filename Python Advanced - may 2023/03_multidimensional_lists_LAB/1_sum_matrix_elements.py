row, col = [int(x) for x in input().split(", ")]
matrix = []
sum_matrix = 0
for idx in range(row):
    matrix.append([int(x) for x in input().split(", ")])
    sum_matrix += sum(matrix[idx])
print(sum_matrix)
print(matrix)
