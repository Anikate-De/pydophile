# Program to check whether a character is alphabet or not.

ch = input('Enter the character - ')

if len(ch) > 1:
    print('Please enter only one character')
else:
    # Using the membership operator
    if ch.lower() in 'abcdefghijklmnopqrstuvwxyz':
        print('Character is a letter in the English Alphabet')
    else:
        print('Character is NOT a letter in the English Alphabet')

    print('-'*10)

    # ALTERNATIVE WAY
    if 97 <= ord(ch.lower()) <= 122:
        print('Character is a letter in the English Alphabet')
    else:
        print('Character is NOT a letter in the English Alphabet')
