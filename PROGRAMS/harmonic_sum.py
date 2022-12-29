# Write a Python program to calculate the harmonic sum of n-1

def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))

# Get the value of n from the user
n = int(input("Enter the value of n: "))

print(harmonic_sum(n-1))