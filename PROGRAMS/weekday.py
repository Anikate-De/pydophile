# Program to input week number and print week day

print('Week numbers are from 1 (Monday) to 7 (Sunday)')

num = int(input('Enter the week number - '))

# Use a chain of if-else statements to print the Matrix
if num == 1:
    print('Monday')
elif num == 2:
    print('Tuesday')
elif num == 3:
    print('Wednesday')
elif num == 4:
    print('Thursday')
elif num == 5:
    print('Friday')
elif num == 6:
    print('Saturday')
elif num == 7:
    print('Sunday')

# ALTERNATIVE WAY
weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekdays[num-1])
