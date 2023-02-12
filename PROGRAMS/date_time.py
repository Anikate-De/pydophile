# A Python program to display the current date and time.

from datetime import datetime

print('The current date and time is', datetime.now())

# Print a formatted datetime string
# FORMAT - dd/mm/YY H:M:S
fmt_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print('The well formatted date and time is', fmt_date)
