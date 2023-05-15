odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    ascii_sum_name = sum(ord(letter) for letter in name) // row

    if ascii_sum_name % 2 == 0:
        even_set.add(ascii_sum_name)
    else:
        odd_set.add(ascii_sum_name)




