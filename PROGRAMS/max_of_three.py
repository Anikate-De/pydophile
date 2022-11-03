# Program to print maximum of 3 numbers

a, b, c = int(input('a - ')), int(input('b - ')), int(input('c - '))

# Maximum using built-in tuple functions in python
print('Maximum value is -', max(a, b, c))


# Max value using conditional statements
print('Max value is -')
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print(a)
