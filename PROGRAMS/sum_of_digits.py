# Program to calculate sum of digits of a non-negative number

# Create a function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Initialize the sum
    sum = 0

    # Calculate the sum of digits
    while number != 0:
        sum += number % 10
        number //= 10

    # Return the sum
    return sum


number = int(input('Enter the number - '))

# Call the function to calculate the sum of digits
sum = sum_of_digits(number)

print('Sum of the digits is', sum)
