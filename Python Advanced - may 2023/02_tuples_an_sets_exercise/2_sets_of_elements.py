first_set_nums, second_set_nums =[int(x) for x in input().split()]
first_set = {int(input()) for _ in range(first_set_nums)}
second_set = {int(input()) for _ in range(second_set_nums)}
result = first_set.intersection(second_set)
print(*result, sep= "\n")