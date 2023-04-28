command = input()
client_list = []
while command != "End":
    if command == "Paid":
        for name in client_list:
            print(name)
        client_list.clear()
    else:
        client_list.append(command)
    command = input()
print(f"{len(client_list)} people remaining.")

