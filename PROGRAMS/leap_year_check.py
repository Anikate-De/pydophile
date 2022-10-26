# Program to find whether a given year is leap or not.


year = int(input('Enter the year - '))

leap = False
if year % 4 == 0:
    leap = True
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True


if leap:
    print(year, 'is a leap year')
else:
    print(year, 'is NOT a leap year')
