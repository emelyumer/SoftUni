from collections import deque
people_in_queue = deque()
quantity_of_water = int(input())
people = input()
while people != "Start":
    people_in_queue.append(people)
    people = input()
command = input().split()
while command[0] != "End":
    if command[0] == "refill":
        quantity_of_water += int(command[1])
    else:
        needed_water = int(command[0])
        if quantity_of_water >= needed_water:
            quantity_of_water -= needed_water
            print(f"{people_in_queue.popleft()} got water")
        else:
            print(f"{people_in_queue.popleft()} must wait")
    command = input().split()
print(f"{quantity_of_water} liters left")
