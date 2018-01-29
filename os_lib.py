import os

print(os.path.abspath('.')) #caminho até chegar neste arquivo
print(os.path.abspath('./test/folder/test_file.py'))
print(os.path.abspath('./test/folder'))

path_test_file = os.path.abspath('./test/folder/test_file.py')
print(os.path.dirname(path_test_file))
print(os.path.exists(path_test_file + '1'))
print(os.path.isfile(path_test_file))
print(os.path.isdir(path_test_file))

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))