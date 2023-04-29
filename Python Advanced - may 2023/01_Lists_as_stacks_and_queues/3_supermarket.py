# command = input()
# client_list = []
# while command != "End":
#     if command == "Paid":
#         for name in client_list:
#             print(name)
#         client_list.clear()
#     else:
#         client_list.append(command)
#     command = input()
# print(f"{len(client_list)} people remaining.")
# second way
from collections import deque
command = input()
client_list = deque()
while command != "End":
    if command == "Paid":
        while client_list:
            print(client_list.popleft())
    else:
        client_list.append(command)
    command = input()
print(f"{len(client_list)} people remaining.")
