#  Write a Python program to add a prefix text to all of the lines in a string

def add_line_prefix(str, prefix):
    lines = str.split('\n')
    for i in range(len(lines)):
        lines[i] = prefix + lines[i]
    return "".join(lines)

print(add_line_prefix(input('Enter the string - '), input('Enter the prefix - ')))

