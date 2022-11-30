# Sort a List According to the Length of the Elements

# Take list input using eval() function
list1 = eval(
    input('Enter the list in correct format [\'apple\',\'book\',\'car\',...]- '))

# Sort the list according to the length of the elements
list1.sort(key=len)

# Print the sorted list
print(list1)
