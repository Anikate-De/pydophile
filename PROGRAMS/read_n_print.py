# Write a Python program to read and print various types of variables.

# For any unknown type of input from the user
print('Unknown Type')
# EVAL function automatically casts into the appropriate type
myVar = eval(input('Enter the value with appropriate syntax - '))
print(myVar)
print('The type of your input is', type(myVar))

# Read and Print a String type
print('String type')
myString = input('Enter the value of the String - ')
print(myString, type(myString))

# Read and Print an Integer type
print('Integer type')
myInt = int(input('Enter the value of the integer - '))
print(myInt, type(myInt))

# Read and Print a Floating type
print('Floating type')
myFloat = float(input('Enter the value of the Floating Point - '))
print(myFloat, type(myFloat))

# Print a Boolean type
print('Boolean type')
myBool = True
print(myBool, type(myBool))

# Read and Print a List type
# EVAL needs an input in the format [1,2,3,...]
print('List type')
myList = eval(input('Enter the value of the List - '))
print(myList, type(myList))

# Read and Print a Tuple type
# EVAL needs an input in the format (1,2,3,...)
print('Tuple type')
myTuple = eval(input('Enter the value of the Tuple - '))
print(myTuple, type(myTuple))

# Read and Print a Set type
# EVAL needs an input in the format {1,2,3,...}
print('Set type')
mySet = eval(input('Enter the value of the Set - '))
print(mySet, type(mySet))

# Read and Print a Dictionary type
# EVAL needs an input in the format {'a':1,'b':2,'c':3,...}
print('Dictionary type')
myDictionary = eval(input('Enter the value of the Dictionary - '))
print(myDictionary, type(myDictionary))
