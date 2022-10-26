#  Program to check if a given integer is a Prime Number or not

num = int(input('Enter the number - '))

for i in range(2, num // 2):
    if num % i == 0:
        print('Entered number is NOT a prime number')
        break
else:
    print('Entered number is a prime number')
