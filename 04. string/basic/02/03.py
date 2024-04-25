input_string = input("Please enter the string you want to reverse: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print("Reversed string from end to start: ", reversed_string)
