import os

path_to_root = os.path.dirname(os.path.abspath(__file__))  #пътя до този файл
file_path = os.path.join(path_to_root, 'file_created_by_python')
try:
    os.remove(file_path)
except FileNotFoundError:
    print('File already deleted!')
else:
    print ("The file_created_by_python has been removed")