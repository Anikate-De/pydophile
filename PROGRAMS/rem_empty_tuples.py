# Write a Python program to remove an empty tuple(s) from a list of tuples

# Get a list of tuples from user
tuples = eval(input("Enter a list of tuples: "))

# Create an empty list to store the non-empty tuples
non_empty = []

# Loop through the list of tuples
for t in tuples:
    # Check if the tuple is empty
    if t:
        # Add the tuple to the list
        non_empty.append(t)

# Print the list
print("Non-empty tuples:", non_empty)