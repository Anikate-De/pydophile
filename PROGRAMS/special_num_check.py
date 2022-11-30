# Program to check whether a number is Armstrong number or Strong or
# Prime Number or Perfect number or magic number or not

print('''PLEASE RUN IN A PYTHON 3.10 INTERPRETER AS THIS PROGRAM USES MATCH-CASE STATEMENTS.
MATCH-CASE (THE PYTHON VERSION OF SWITCH-CASE) WAS INTRODUCED IN 3.10
INTERPRETERS <= 3.9 WILL GIVE A SYNTAX ERROR''')

def armstrong_check(n):
    digits = 0
    temp = num
    while temp > 0:
        digits += 1
        temp = temp // 10

    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if num == sum:
        print('Entered number is an armstrong number')
    else:
        print('Entered number is NOT an armstrong number')


def prime_check(n):
    for i in range(2, n // 2):
        if n % i == 0:
            print('Entered number is NOT a prime number')
            break
    else:
        print('Entered number is a prime number')


def perfect_check(n):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n:
        print('Entered number is a perfect number')
    else:
        print('Entered number is NOT a perfect number')
    pass


def magic_check(n):
    digitCount = len(str(n))
    sumOfDigits = 0

    temp = n

    while (digitCount > 1):

        sumOfDigits = 0

        while (temp > 0):
            sumOfDigits += temp % 10
            temp = temp//10

        temp = sumOfDigits
        digitCount = len(str(sumOfDigits))

    if (sumOfDigits == 1):
        print('Entered number is a magic number')
    else:
        print('Entered number is NOT a magic number')
    pass


num = int(input('Enter the number - '))

print('Enter the corressponding number for the checks below -')
print('1. Armstrong Number Check')
print('2. Prime Number Check')
print('3. Perfect Number Check')
print('4. Magic Number Check')
print('Enter any number for all checks')

choice = int(input('Your choice - '))

match choice:
    case 1:
        print('Checking for Armstrong Number')
        armstrong_check(num)
    case 2:
        print('Checking for Prime Number')
        prime_check(num)
    case 3:
        print('Checking for Perfect Number')
        perfect_check(num)
    case 4:
        print('Checking for Magic Number')
        magic_check(num)
    case other:
        print('Performing all checks')
        armstrong_check(num)
        prime_check(num)
        perfect_check(num)
        magic_check(num)
