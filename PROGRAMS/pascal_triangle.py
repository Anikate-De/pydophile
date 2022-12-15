# Write a Python function that prints out the first n rows of Pascal's triangle.

def pascal_triangle(n):
    # Create a list of lists to store the values of Pascal's triangle
    pascal = [[1]] * n

    # Fill the list of lists with the values of Pascal's triangle
    for i in range(1, n):
        pascal[i] = [1] * (i + 1)
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    # Print the values of Pascal's triangle
    for i in range(n):
        print("  "*(n-i), end="")
        for j in range(i + 1):
            print(pascal[i][j], end="   ")
        print()

# Get the value of n from the user
n = int(input("Enter the number of rows: "))

pascal_triangle(n)