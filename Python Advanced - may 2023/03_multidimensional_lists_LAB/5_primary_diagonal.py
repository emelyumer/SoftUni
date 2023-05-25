rows = int(input())
matrix = [[int(col) for col in input().split()] for row in range(rows)]
# print(matrix)
sum_diagonal = 0

for index in range(rows):
    sum_diagonal += matrix[index][index]
print(sum_diagonal)
