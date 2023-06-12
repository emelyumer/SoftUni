def move(way):
    check_pos = [e_pos[0] + directions[way][0], e_pos[1] + directions[way][1]]
    if 0 <= check_pos[0] < SIZE and 0 <= check_pos[1] < SIZE:
        return check_pos

    elif not 0 <= check_pos[0] < SIZE:
        if check_pos[0] < 0:
            check_pos[0] = 5
        elif check_pos[0] > 5:
            check_pos[0] = 0
        return check_pos

    elif not 0 <= check_pos[1] < SIZE:
        if check_pos[1] < 0:
            check_pos[1] = 5
        elif check_pos[1] > 5:
            check_pos[1] = 0
        return check_pos


SIZE = 6
matrix = [input().split() for r in range(SIZE)]
water_deposit = False
metal_deposit = False
concrete_deposit = False
e_pos = []
rover_broken = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for idx_r in range(len(matrix)):
    if "E" in matrix[idx_r]:
        e_pos =[idx_r, matrix[idx_r].index("E")]
        break

while not rover_broken:
    for command in input().split(', '):
        check_move = move(command)
        e_pos = check_move
        if matrix[e_pos[0]][e_pos[1]] == "W":
            water_deposit = True
            print(f"Water deposit found at ({', '.join(str(x) for x in e_pos)})")

        elif matrix[e_pos[0]][e_pos[1]] == "M":
            metal_deposit = True
            print(f"Metal deposit found at ({', '.join(str(x) for x in e_pos)})")

        elif matrix[e_pos[0]][e_pos[1]] == "C":
            concrete_deposit = True
            print(f"Concrete deposit found at ({', '.join(str(x) for x in e_pos)})")

        elif matrix[e_pos[0]][e_pos[1]] == "R":
            rover_broken = True
            print(f"Rover got broken at ({', '.join(str(x) for x in e_pos)})")
    else:
        break


if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


