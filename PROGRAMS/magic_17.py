# Write a Python program to get the difference between a given number and 17
# if the number is greater than 17 return double the absolute difference

n = int(input('Enter a number - '))

if n > 17:
    print('Double of absolute difference from 17 is', abs(n-17)*2)
else:
    print('Difference from 17 is', abs(n-17))
