import os

path_to_root = os.path.dirname(os.path.abspath(__file__))  #пътя до този файл
file_path = os.path.join(path_to_root, "text.txt")         #пътя до търсения файл
if os.path.isfile(file_path):
    print('File found')
else:
    print('File not found')

try:
    file = open(file_path, "r")
    print(file.readline()) # тази команда дава автоматично нов ред след изпълнението си
    print(file.readline()) # тази команда дава автоматично нов ред след изпълнението си
    print(file.read())


except FileExistsError:
    print('File not found')

else:
    print('File found')


