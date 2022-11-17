# Program to count total number of notes in given amount

amt = int(input('Enter the amount - '))

denominations = {
    2000: 0,
    500: 0,
    200: 0,
    100: 0,
    50: 0,
    20: 0,
    10: 0
}

# Run a loop till amount is exhausted
while amt > 0:
    # Check if the amount is greater than any of the valid denominations
    # Subtract the denomination and increase notes by 1
    if amt >= 2000:
        amt -= 2000
        denominations[2000] += 1
    elif amt >= 500:
        amt -= 500
        denominations[500] += 1
    elif amt >= 200:
        amt -= 200
        denominations[200] += 1
    elif amt >= 100:
        amt -= 100
        denominations[100] += 1
    elif amt >= 50:
        amt -= 50
        denominations[50] += 1
    elif amt >= 20:
        amt -= 20
        denominations[20] += 1
    elif amt >= 10:
        amt -= 10
        denominations[10] += 1
    else:
        # If the amount is no longer deductible, print the amount
        # As it is present only in coins
        print('Amount present in coins', amt)
        break

notes = 0

for key, value in denominations.items():
    if value > 0:
        print(value, '-', key, 'notes')
        notes += value

print('Number of notes present in the amount is', notes)