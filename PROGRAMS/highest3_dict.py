# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

# Get a dictionary from user
d = eval(input("Enter a dictionary: "))

# Create an empty list to store the values
values = []

# Sort the dictionary by values in descending order
for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
    # Add the value to the list
    values.append((k,v))

# Print the highest 3 values
print("Highest 3 values: (Key, Value)", values[:3])