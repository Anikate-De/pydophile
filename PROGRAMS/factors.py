# Program to find all factors of a number.

num = int(input('Enter the number - '))
factors = []
for i in range(1, num+1):
    if num % i == 0:
        factors += [i]

print('Factors are -', factors)
