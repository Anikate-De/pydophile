# Program to find the second largest number in a list
n = eval(input('Enter the list in correct format [1,2,3,...]- '))

largest = n[0]
second_largest = n[0]
for i in n:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i

print('The second largest number in the list is', second_largest)
