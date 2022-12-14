# Program to merge two lists and sort it

n1 = eval(input('Enter the first list in correct format [1,2,3,...]- '))
n2 = eval(input('Enter the second list in correct format [1,2,3,...]- '))

# Merge the two lists by simply using the plus (concatenation) operator
n = n1 + n2

n.sort()

# Print the sorted list
print(n)
