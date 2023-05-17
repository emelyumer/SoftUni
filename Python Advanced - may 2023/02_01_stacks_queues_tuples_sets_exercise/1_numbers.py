first_set = {int(x) for x in input().split()}
second_set = {int(y) for y in input().split()}

for index in range(int(input())):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            for idx in range(2, len(command)):
                number = int(command[idx])
                first_set.add(number)
        elif command[1] == "Second":
            for idx in range(2, len(command)):
                number = int(command[idx])
                second_set.add(number)
    elif command[0] == "Remove":
        if command[1] == "First":
            for idx in range(2, len(command)):
                number = int(command[idx])
                if number in first_set:
                    first_set.remove(number)
        elif command[1] == "Second":
            for idx in range(2, len(command)):
                number = int(command[idx])
                if number in second_set:
                    second_set.remove(number)
    elif command[0] == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")
result1 = sorted(first_set)
result2 = sorted(second_set)
print(*result1, sep=", ")
print(*result2, sep=", ")
