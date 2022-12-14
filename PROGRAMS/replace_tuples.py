# Write a Python program to replace last value of tuples in a list.

# Get a list of tuples from user
tuples = eval(input("Enter a list of tuples: "))

# Create an empty list to store the tuples
new_tuples = []

for t in tuples:
    # Create an empty list to store the items of the tuple
    items = []
    
    # Loop through the tuple
    for i in t:
        # Add the item to the list
        items.append(i)
        
    # Replace the last item with 100
    items[-1] = 100
    
    # Convert the list to a tuple
    t = tuple(items)
    
    # Add the tuple to the list
    new_tuples.append(t)

# Print the list
print("New list of tuples:", new_tuples)