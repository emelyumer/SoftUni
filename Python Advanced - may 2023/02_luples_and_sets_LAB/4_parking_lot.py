number_of_commands = int(input())
parking_lot = set()
for _  in range(number_of_commands):
    command, car_number = input().split(", ")
    if command == "IN":
        parking_lot.add(car_number)
    elif command == "OUT":
        parking_lot.remove(car_number)
if parking_lot:
    print('\n'.join(parking_lot))
else:
    print("Parking Lot is Empty")
