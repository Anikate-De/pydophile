# Program to test whether a number is within 100 of 1000 or 2000

num = int(input('Enter the number - '))

# Check if the absolute difference between the number and 1000 is less than 100
if abs(num-1000) <= 100:
    print(num, 'is close to 1000')
# Else if the absolute difference between the number and 2000 is less than 100
elif abs(num-2000) <= 100:
    print(num, 'is close to 2000')
else:
    print(num,'is neither close to 1000 nor 2000')
