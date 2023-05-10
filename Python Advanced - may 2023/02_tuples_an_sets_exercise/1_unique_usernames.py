# n_lines = int(input())
# unique_usernames = set()
# for _ in range(n_lines):
#     username = input()
#     unique_usernames.add(username)
# print('\n'.join(unique_usernames))

#втори по-кратък вариант
unique_usernames = {input() for _ in range(int(input()))}
print(*unique_usernames, sep= "\n")