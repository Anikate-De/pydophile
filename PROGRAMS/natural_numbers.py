# Program to print all natural numbers from 1 to n. - using while loop

number = int(input("Please Enter any Number: "))
i = 1

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

#Using While Loop we iterate over the range from 1 to n and print the required output.

while ( i <= number):
    print (i, end = '  ')
    i = i + 1

