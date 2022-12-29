# Write a Python program to find  the greatest common divisor (gcd) of two integers using Recursion

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# Get the numbers from the user
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print(gcd(m, n))