row = int(input())
flatten_matrix = []
for idx in range(row):
    flatten_matrix.extend([int(x) for x in input().split(", ")])
print(flatten_matrix)