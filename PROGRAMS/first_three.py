# Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string

def first_three(str):
    if len(str) < 3:
        return str
    else:
        return str[:3]

print(first_three(input('Enter a string - ')))
