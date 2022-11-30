'''
    Python program to print 'n' terms of the fibonacci series, where
    'n' is the integer input by the user
'''

# Get user input
n = int(input("Enter the number of terms - "))

# First two terms of the fibonacci series, essential for printing the series
a, b = 0, 1

if n <= 0:
    print("Please enter a natural number, i.e, 1, 2, 3, ...")
elif n == 1:
    print("Fibonacci sequence upto", n, "terms is:")
    print(a)
else:
    print("Fibonacci sequence upto", n, "terms is:")
    while n > 0:
        print(a)
        next = a + b
        a = b
        b = next
        n = n-1
