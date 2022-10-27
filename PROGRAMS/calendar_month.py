# Write a Python program to print the calendar of a given month and year.

import calendar

# Get the user input for year and month
year = int(input('Enter the year - '))
month = int(input('Enter the two digit number for the month - '))
   
# Display the calendar
print(calendar.month(year, month))
