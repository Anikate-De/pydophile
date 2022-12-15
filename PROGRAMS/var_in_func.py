# Write a Python program to detect the number of local variables declared in a function

# Create a function for demonstration purposes
def hello():
    a = 1
    b = 2
    c = 3
    print(a, b, c)

print("Number of variables in the function,", '\''+hello.__name__+'\'', "is", hello.__code__.co_nlocals)