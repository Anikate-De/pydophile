# Python Program to Swap Two Variables

a = int(input('Enter the value of a - '))
b = int(input('Enter the value of b - '))

print('Value of a before swapping -', a)
print('Value of b before swapping -', b)

# Swapping Logic

print('By using a temporary variable to swap')
# With temporary variable
c = a
a = b
b = c

print('Value of a after swapping -', a)
print('Value of b after swapping -', b)

print('By the method of tuple unpacking')
# With Tuple unpacking
a, b = b, a

print('Value of a after swapping again -', a)
print('Value of b after swapping again -', b)

print('By performing mathematical operations')
# With mathematical operations
a = b + a
b = a-b
a = a-b

print('Value of a after swapping again -', a)
print('Value of b after swapping again -', b)
