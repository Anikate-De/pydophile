# Write a Python program to read and print various types of variables.

print('Unknown Type')
myVar = eval(input('Enter the value with appropriate syntax - '))
print(myVar)
print('The type of your input is', type (myVar))

print('String type')
myString = input('Enter the value of the String - ')
print(myString, type(myString))

print('Integer type')
myInt = int(input('Enter the value of the integer - '))
print(myInt, type(myInt))

print('Floating type')
myFloat = float(input('Enter the value of the Floating Point - '))
print(myFloat, type(myFloat))

print('Boolean type')
myBool = bool(input('Enter the value of the Boolean - '))
print(myBool, type(myBool))

print('List type')
myList = eval(input('Enter the value of the List - '))
print(myList, type(myList))

print('Tuple type')
myTuple = eval(input('Enter the value of the Tuple - '))
print(myTuple, type(myTuple))

print('Set type')
mySet = eval(input('Enter the value of the Set - '))
print(mySet, type(mySet))

print('Dictionary type')
myDictionary = eval(input('Enter the value of the Dictionary - '))
print(myDictionary, type(myDictionary))
