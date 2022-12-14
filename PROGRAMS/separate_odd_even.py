# Program to separate odd and even numbers in a list

n = eval(input('Enter the list in correct format [1,2,3,...]- '))

odd = []
even = []

for i in n:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print('The odd numbers in the list are', odd)
print('The even numbers in the list are', even)
