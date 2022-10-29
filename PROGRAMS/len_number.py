# Program to count number of digits in a number

number = int(input('Enter the number - '))

digits = 0
# Create a temporary copy of the entered number
temp = number
while temp>0:
    digits += 1
    temp //= 10

print(digits)


# ALTERNATIVE WAY

print(len(str(number)))
