# Write a Python Program to Form a New String where the First Character and the Last Character have been Exchanged.

# Get the string from user input
string = input('Enter a string - ')

# Extract the first and last characters
first = string[0]
last = string[-1]

# Form the new string
new_string = last + string[1:-1] + first

# Display the new string
print('The new string is', new_string)