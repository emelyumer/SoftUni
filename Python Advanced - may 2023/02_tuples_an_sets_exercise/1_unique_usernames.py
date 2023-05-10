# n_lines = int(input())
# unique_usernames = set()
# for _ in range(n_lines):
#     username = input()
#     unique_usernames.add(username)
# print('\n'.join(unique_usernames))

n_lines = int(input())
unique_usernames = {}
for _ in range(n_lines):
    username = input()
    unique_usernames.add(username)
print('\n'.join(unique_usernames))