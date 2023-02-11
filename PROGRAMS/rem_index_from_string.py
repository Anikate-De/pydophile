# Write a Python Program to Remove the nth Index Character from a Non-Empty String
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


# Get string from user input
str = input("Enter a string: ")

# Get index from user input
n = int(input("Enter index to remove: "))

# Print the new string
print("New string: ", remove_char(str, n))
