# Program to check whether a number is palindrome or not

number = int(input('Enter the number - '))

temp = number
rev = 0

while temp > 0:
    rev *= 10
    rev += temp%10
    temp//=10

if rev == number:
    print('Number is a Palindrome')
else:
    print('Number is NOT a Palindrome')
