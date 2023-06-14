import os

path_to_root = os.path.dirname(os.path.abspath(__file__))  #пътя до този файл
file_path = os.path.join(path_to_root, "numbers.txt")         #пътя до търсения файл
if os.path.isfile(file_path):
    print('File found')
else:
    print('File not found')

try:
    file = open(file_path, "r")
    content_lines = file.read().split("\n")
    number = [int(el) for el in content_lines if el]
    print(sum(number))


except FileExistsError:
    print('File not found')

else:
    print('File found')


