# Print all odd indexed elements of a list

# Take list input using eval() function
list1 = eval(input('Enter the list in correct format [1,2,3,...]- '))

# Create an empty list to store the odd indexed elements
odd_index = []

# Iterate over the list and append the odd indexed elements to the list
for i in range(len(list1)):
    if i % 2 != 0:
        odd_index.append(list1[i])

# Print the odd indexed elements list
print(odd_index)
