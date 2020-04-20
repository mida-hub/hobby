import os

file_name = 'test1/test2/test3.txt'

print(f'dirname: {os.path.dirname(file_name)}')
print(f'filename: {os.path.basename(file_name)}')
print(f'ext: {os.path.splitext(file_name)[1]}')