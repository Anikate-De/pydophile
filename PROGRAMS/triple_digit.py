# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

# Get the user input
n = int(input('Enter the value of \'n\' - '))

print('Value of n + nn + nnn is')

value = n + int(str(n)*2) + int(str(n)*3)

print(value)


# ALTERNATIVE WAY, USING A `FOR IN RANGE` LOOP
value = 0
for i in range(3):
    value += int(str(n)*(i+1))

print(value)
