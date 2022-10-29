# Program to find sum of all odd numbers between 1 to n

n = int(input('Enter the value of n - '))

# Declare a variable to store the value of the sum
sum = 0
num = 2
while num<n:
    if not num%2==0:
        sum+=num
    num+=1

print('Sum of all odd numbers BETWEEN 1 AND', n, 'is', sum)
