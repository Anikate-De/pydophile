# A program to calculate the sum of three given numbers
# If the values are equal then return three times of their sum

a, b, c = int(input('a - ')), int(input('b - ')), int(input('c - '))

if a == b == c:
    print('Three times their sum is', (a+b+c)*3)
else:
    print('Their sum is', (a+b+c))
