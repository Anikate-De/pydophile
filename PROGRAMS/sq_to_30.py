# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def sq_to_30():
    # Create a list to store the values
    squares = []

    # Fill the list with the values
    for i in range(1, 31):
        squares.append(i ** 2)

    # Print the values
    print(squares)


sq_to_30()
