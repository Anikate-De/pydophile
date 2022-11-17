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


# ALTERNATIVELY

# Find the first digit; defining a function "firstDigit(n)"
def firstDigit(n):

    # Remove last digit from number
    # till only one digit is left
    while n >= 10:
        n = n / 10

    # return the first digit
    return int(n)

# Find the last digit; defining a function "lastDigit(n)"


def lastDigit(n):

    # return the last digit
    return (n % 10)


# Execution code; declare number and print output.
print(firstDigit(number), end=" ")
print(lastDigit(number))