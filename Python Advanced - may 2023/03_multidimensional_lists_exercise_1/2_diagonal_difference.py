rows = int(input())
matrix = [[int(x) for x in input().split()] for r in range(rows)]
primary_diagonal = [matrix[row_idx][row_idx] for row_idx in range(rows)]
secondary_diagonal = [matrix[row_idx][rows - row_idx -1] for row_idx in range(rows)]
# for row_idx in range(rows):
#     element = matrix[row_idx][row_idx]
#     primary_diagonal.append(element)
# for row_idx in range(rows):
#     sec_element = matrix[row_idx][rows - row_idx - 1]
#     secondary_diagonal.append(sec_element)
result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)


