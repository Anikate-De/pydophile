# Program to Find the Factorial of a Number

# Input the number
num = int(input('Enter the number - '))

fact = 1
temp = 1
# Run a loop from 1 to the number
while temp <= num:
    fact *= temp
    temp += 1

# Print the factorial
print('Factorial is', fact)
