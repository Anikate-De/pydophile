# Program to find first and last digit of a number

number = int(input('Enter the number - '))

digits = 0
# Create a temporary copy of the entered number
temp = number
while temp>0:
    digits += 1
    temp //= 10

print('First Digit -', number//(10**(digits-1)))
print('Last Digit -', number%10)
