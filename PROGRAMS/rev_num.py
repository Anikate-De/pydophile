# Program to enter a number and print its reverse

number = int(input('Enter the number - '))

rev = 0
while number > 0:
    rev *= 10
    rev += number%10
    number//=10

print('Reverse of the number is', rev)
