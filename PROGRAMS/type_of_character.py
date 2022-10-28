# Program to input any character and check whether it is alphabet, digit or special character.

ch = input('Enter the character - ')

if len(ch) > 1:
    print('Please enter only one character')
else:
    # Using the membership operator
    if ch.lower() in 'abcdefghijklmnopqrstuvwxyz':
        print('Character is a letter in the English Alphabet')
    elif ch in '0123456789':
        print('Character is a Number')
    elif ch in '!@#$%^&*()_+-={][}|\\:;\'\",<.>?/`~':
        print('Entered character is a special character')
