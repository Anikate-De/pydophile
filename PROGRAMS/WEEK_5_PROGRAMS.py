#1. Write a Python program to print all natural numbers from 1 to n. - using while loop
number = int(input("Please Enter any Number: "))
i = 1

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

#Using While Loop we iterate over the range from 1 to n and print the required output.

while ( i <= number):
    print (i, end = '  ')
    i = i + 1


#2. Write a Python program to find sum of all odd numbers between 1 to n.
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

#Using For Loop we give the range between 1 to n
#to find sum of all odd numbers in that range

for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal)) 


#3. Write a Python program to count number of digits in a number.
num = 1215
count = 0
#Using While Loop; where number not equal to zero
#we perform the required task of counting
while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))


#4. Write a Python program to find first and last digit of a number.
# Find the first digit; defining a function "firstDigit(n)"
def firstDigit(n) :
 
    # Remove last digit from number
    # till only one digit is left
    while n >= 10:
        n = n / 10;
     
    # return the first digit
    return int(n)
 
# Find the last digit; defining a function "lastDigit(n)"
def lastDigit(n) :
 
    # return the last digit
    return (n % 10)
 
# Execution code; declare number and print output.
n = 45603;
print(firstDigit(n), end = " ")
print(lastDigit(n))

#5. Write a Python program to calculate sum of digits of a number.
#Defining Function getSum(n)
def getSum(n):
    
    #Using For loop on the string.
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 12345
print(getSum(n))


#6. Write a Python program to enter a number and print its reverse.
n=int(input("Enter number: "))
rev=0
#Using While Loop last number is obtained by using the modulus operator
#last digit then stored at one's place, second last at ten's and so on
#last digit is removed by truly dviding it by 10; loop terminates when num=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)