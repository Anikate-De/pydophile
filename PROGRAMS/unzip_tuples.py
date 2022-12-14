# Write a Python program to unzip a list of tuples into individual lists.

# Get a list of tuples from user
tuples = eval(input("Enter a list of tuples: "))

# Create an empty list to store the unzipped tuples
unzipped = []

# Get the length of the tuples
length = len(tuples[0])

# Loop from 0 to the length of the tuples-1
for i in range(length):
    # Create an empty list to store the items of the tuple
    elements = []

    # Loop through the list of tuples
    for t in tuples:
        # Add the item to the list
        elements.append(t[i])

    # Add the list to the list of unzipped tuples
    unzipped.append(tuple(elements))

# Print the list of unzipped tuples
print(unzipped)