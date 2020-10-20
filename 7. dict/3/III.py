keys = ['fname', 'lname', 'age']
values = ['MohammadReza', 'Kasaie', 23]
res = {k: values[index] for index, k in enumerate(keys)}
print(res)
