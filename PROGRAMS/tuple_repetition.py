# Write a Python program to find the repeated items of a tuple.

# Get a tuple from user
t = eval(input("Enter a tuple: "))

# Create an empty list to store repeated items
repeated = []

# Loop through the tuple
for i in t:
    # Check if the item is already in the list
    if i in repeated:
        continue
    # Check if the item is repeated
    if t.count(i) > 1:
        # Add the item to the list
        repeated.append(i)

# Print the list
print("Repeated items:", repeated)