from collections import deque
number_of_petrol_pumps = int(input())
petrol_pump_list = deque(list())

tank = 0
index = 0
for idx in range(number_of_petrol_pumps):
    petrol_pump = input().split()
    petrol_pump_list.append(petrol_pump)

used_list = petrol_pump_list.copy()

while used_list:
    lr = int(used_list[0][0])
    km = int(used_list[0][1])
    tank += lr
    if tank >= km:
        tank -= km
        used_list.popleft()
    else:
        petrol_pump_list.rotate(-1)
        used_list = petrol_pump_list.copy()
        index += 1
        tank = 0
print(index)
