def move(direction):
    santa_row = santa_position[0] + directions[direction][0]
    santa_col = santa_position[1] + directions[direction][1]
    if not (0 <= santa_row < size and 0 <= santa_col < size):
        return santa_position
    return [santa_row, santa_col]


def check_for_lucky_kids():
    check_pos = []
    check_pos = move("left")
    if neighborhood[check_pos[0]][check_pos[1]] == "V" or neighborhood[check_pos[0]][check_pos[1]] == "X":
        lucky_kids_list.append(check_pos)
    check_pos = move("right")
    if neighborhood[check_pos[0]][check_pos[1]] == "V" or neighborhood[check_pos[0]][check_pos[1]] == "X":
        lucky_kids_list.append(check_pos)
    check_pos = move("up")
    if neighborhood[check_pos[0]][check_pos[1]] == "V" or neighborhood[check_pos[0]][check_pos[1]] == "X":
        lucky_kids_list.append(check_pos)
    check_pos = move("down")
    if neighborhood[check_pos[0]][check_pos[1]] == "V" or neighborhood[check_pos[0]][check_pos[1]] == "X":
        lucky_kids_list.append(check_pos)
    return lucky_kids_list


gifts = int(input())
size = int(input())
neighborhood = []
santa_position = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
nice_kids = 0
nice_kids_with_gifts = 0
lucky_kids_list = []
available_gifts = True

for index in range(size):
    neighborhood.append(input().split())
    if "S" in neighborhood[index]:
        santa_position = [index, neighborhood[index].index("S")]
        neighborhood[santa_position[0]][santa_position[1]] = "-"
    if "V" in neighborhood[index]:
        nice_kids += neighborhood[index].count("V")

while True:
    if gifts == 0:
        available_gifts = False
        break
    command = input()
    if command == "Christmas morning":
        break
    santa_position = move(command)
    if neighborhood[santa_position[0]][santa_position[1]] == "C":
        lucky_kids_list = check_for_lucky_kids()
        for idx in range(len(lucky_kids_list)):
            if gifts == 0:
                available_gifts = False
                break
            if neighborhood[lucky_kids_list[idx][0]][lucky_kids_list[idx][1]] == "V":
                nice_kids_with_gifts += 1
            neighborhood[lucky_kids_list[idx][0]][lucky_kids_list[idx][1]] = "-"
            gifts -= 1

    elif neighborhood[santa_position[0]][santa_position[1]] == "V":
        neighborhood[santa_position[0]][santa_position[1]] = "-"
        gifts -= 1
        nice_kids_with_gifts += 1
    elif neighborhood[santa_position[0]][santa_position[1]] == "X":
        neighborhood[santa_position[0]][santa_position[1]] = "-"

    if not available_gifts:
        break

neighborhood[santa_position[0]][santa_position[1]] = "S"
if nice_kids == nice_kids_with_gifts:
    print(*[' '.join(row) for row in neighborhood], sep="\n")
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
elif not gifts:
    print(f"Santa ran out of presents!")
if nice_kids > nice_kids_with_gifts:
    print(*[' '. join(row) for row in neighborhood], sep="\n")
    print(f"No presents for {nice_kids - nice_kids_with_gifts} nice kid/s.")





