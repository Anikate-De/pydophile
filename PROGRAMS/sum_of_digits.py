# Program to calculate sum of digits of a number

number = int(input('Enter the number - '))

sum = 0
while number > 0:
    sum += number%10
    number//=10

print('Sum of the digits is', sum)
