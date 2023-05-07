n = int(input())
names = list()
for _ in range(n):
    name = input()
    names.append(name)
unique_names = set(names)
print('\n'.join(unique_names))