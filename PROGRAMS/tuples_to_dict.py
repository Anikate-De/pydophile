# Write a Python program to convert a list of tuples into a dictionary.

# Get a list of tuples from user
tuples = eval(input("Enter a list of tuples: "))

# Create an empty dictionary
d = {}

# Loop through the list of tuples
for t in tuples:
    # Add the tuple to the dictionary
    d[t[0]] = t[1]

# Print the dictionary
print("Dictionary:", d)