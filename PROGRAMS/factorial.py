# Program to calculate factorial of a number.

num = int(input('Enter the number - '))

if num < 0:
    print('Factorial is not defined')
else:
    fact = 1
    for i in range(num):
        fact *= (i+1)
    print('Factorial is', fact)
