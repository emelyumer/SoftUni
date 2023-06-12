def check_diagonals_w(w_p):
    left_check_pos = [w_p[0] + directions["left_d_w"][0],  w_p[1] + directions["left_d_w"][1]]
    right_check_pos = [w_p[0] + directions["right_d_w"][0], + w_p[1] + directions["right_d_w"][1]]
    if left_check_pos == black_pos or right_check_pos == black_pos:
        return True


def check_diagonals_b(b_p):
    left_check_pos = [b_p[0] + directions["left_d_b"][0], b_p[1] + directions["left_d_b"][1]]
    right_check_pos = [b_p[0] + directions["right_d_b"][0], b_p[1] + directions["right_d_b"][1]]
    if left_check_pos == white_pos or right_check_pos == white_pos:
        return True


directions = {
    "left_d_w": (-1, -1),
    "right_d_w": (-1, 1),
    "left_d_b": (1, -1),
    "right_d_b": (1, 1),
}

SIZE = 8
matrix = [input().split() for r in range(8)]

white_pos = []
black_pos = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
list_num = [8, 7, 6, 5, 4, 3, 2, 1]
for idx_row in range(len(matrix)):
    if 'w' in matrix[idx_row]:
        white_pos = [idx_row, matrix[idx_row].index('w')]
    if 'b' in matrix[idx_row]:
        black_pos = [idx_row, matrix[idx_row].index('b')]

for index_r in range(len(list_num)):
    for index_c in range(len(letters)):
        matrix[index_r][index_c] = letters[index_c] + str(list_num[index_r])


while True:
    ok_attack_pos = check_diagonals_w(white_pos)
    if ok_attack_pos:
        print(f"Game over! White win, capture on {matrix[black_pos[0]][black_pos[1]]}.")
        break
    white_next_pos = [white_pos[0] - 1, white_pos[1]]
    if white_next_pos[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {matrix[white_next_pos[0]][white_next_pos[1]]}.")
        break
    white_pos = white_next_pos

    ok_attack_pos = check_diagonals_b(black_pos)
    if ok_attack_pos:
        print(f"Game over! Black win, capture on {matrix[white_pos[0]][white_pos[1]]}.")
        break
    black_next_pos = [black_pos[0] + 1, black_pos[1]]
    if black_next_pos[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {matrix[black_next_pos[0]][black_next_pos[1]]}.")
        break
    black_pos = black_next_pos
