import os

path_to_root = os.path.dirname(os.path.abspath(__file__))  #пътя до този файл
file_path = os.path.join(path_to_root, 'file_created_by_python')
with open('file_created_by_python', "w") as file:
    file.write('I just created my first file!')