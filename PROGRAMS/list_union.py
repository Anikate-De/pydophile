# Find the Union of two Lists

# Take list input using eval() function
list1 = eval(input('Enter the first list in correct format [1,2,3,...]- '))
list2 = eval(input('Enter the second list in correct format [1,2,3,...]- '))

# Create an empty list to store the union of the two lists
union = []

# Iterate over the first list and append the elements to the union list
for i in list1:
    union.append(i)

# Iterate over the second list and append the elements to the union list
for i in list2:
    if i not in list1:
        union.append(i)

# Print the union list
print(union)
