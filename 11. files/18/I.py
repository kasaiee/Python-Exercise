lines = open('../sample-code.py').readlines()
lines = [line.split('#')[0] + '\n' if '#' in line else line for line in lines]
open('sample-code-without-comment.py', 'w').writelines(lines)