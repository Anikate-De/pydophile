# A Program which will find all such numbers which are divisible by 7 but are not a multiple of 5
# Between 2000 and 3200 (both included)
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Consider use range(#begin, #end) method

for num in range(2000,3001):
    # Check for divisibility by 7 and indivisibility by 5
    if num%7 ==0 and not num%5==0:
        # Use end parameter of the Print statement to change the end character
        # The default character is `\n` (newline)
        print(num, end=',')
