# Program to check whether a number is divisible by 5 and 11 or not.

# Take input
num = int(input('Enter the number - '))

if num%5==0 and num%11==0:
    print(num, 'is divisible by both 5 and 11')
else:
    print(num, 'is NOT divisible by both 5 and 11')
