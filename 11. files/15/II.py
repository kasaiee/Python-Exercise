import os


file_names = [file_name for file_name in os.listdir() if file_name[:4] == 'test']
result = ''.join([open(file_name).read() for file_name in file_names ])
open('merged-file.txt', 'w').write(result)