# Write a Python Program to Detect if Two Strings are Anagrams

# Get the first string from user input
first = input('Enter the first string - ')

# Get the second string from user input
second = input('Enter the second string - ')

# Check if first and second are anagrams
if sorted(first.lower()) == sorted(second.lower()):
    print('The strings are anagrams.')
else:
    print('The strings are not anagrams.')