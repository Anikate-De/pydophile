# Program to find sum of all odd numbers between 1 to n.
maximum = int(input(" Please Enter the Maximum Value : "))
oddTotal = 0

# Using For Loop we give the range between 1 to n
# to find sum of all odd numbers in that range

for number in range(1, maximum+1):
    if (number % 2 != 0):
        print("{0}".format(number))
        oddTotal = oddTotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, oddTotal))
