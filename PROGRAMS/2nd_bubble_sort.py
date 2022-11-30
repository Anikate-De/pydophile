# Find the Second Largest Number in a List Using Bubble Sort

# Take list input using eval() function
n = eval(input('Enter the list in correct format [1,2,3,...]- '))

# Sort the list using bubble sort
for i in range(len(n)):
    for j in range(len(n) - 1):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]

# Print the second largest number in the list
print('The second largest number in the list is', n[-2])
