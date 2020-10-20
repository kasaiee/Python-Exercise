import os


file_names = [file_name for file_name in os.listdir() if file_name[:4] == 'test']
result = ''
for file_name in file_names:
    result += open(file_name).read()
open('merged-file.txt', 'w').write(result)
