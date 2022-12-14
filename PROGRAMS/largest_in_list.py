# Program to find the largest number in the list

n = eval(input('Enter the list in correct format [1,2,3,...]- '))

largest = n[0]
for i in n:
    if i > largest:
        largest = i

print('The largest number in the list is', largest)
