# matrix = [[int(x) for x in row.split()]for row in input().split("|")]
# new = []
# [new.extend(el) for el in matrix[::-1]]
# print(*new)

#2nd way
matrix = [row.split()for row in input().split("|")]
print(*[' '.join(sublist) for sublist in matrix[::-1] if sublist])