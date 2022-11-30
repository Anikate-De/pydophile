# Find the Intersection of Two Lists

# Take list input using eval() function
list1 = eval(input('Enter the first list in correct format [1,2,3,...]- '))
list2 = eval(input('Enter the second list in correct format [1,2,3,...]- '))

# Create an empty list to store the intersection of the two lists
intersection = []

# Iterate over the first list and append the elements to the intersection list
for i in list1:
    if i in list2:
        intersection.append(i)

# Print the intersection list
print(intersection)
