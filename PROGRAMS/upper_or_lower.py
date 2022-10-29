# Program to check whether a character is uppercase or lowercase alphabet

ch = input('Enter the character - ')

if len(ch) > 1:
    print('Please enter only one character')
else:
    if ch.islower():
        print('Character is lowercase')
    else:
        print('Character is uppercase')
