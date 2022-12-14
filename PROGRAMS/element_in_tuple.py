# Write a Python program to check whether an element exists within a tuple

# Get a tuple from user
t = eval(input("Enter a tuple: "))

# Get an item from user
item = eval(input("Enter an item: "))

# Check if the item is in the tuple
if item in t:
    print("Item exists in the tuple")
else:
    print("Item does not exist in the tuple")
