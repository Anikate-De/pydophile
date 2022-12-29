# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)

def recursive_series(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_series(n - 2)

# Get the value of n from the user
n = int(input("Enter the value of n: "))

print(recursive_series(n))