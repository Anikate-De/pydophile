# Program to count total number of notes in given amount

amt = int(input('Enter the amount - '))

# Create a variable to store the number of notes present in the amount
notes = 0

# Run a loop till amount is exhausted
while amt>0:
    # Check if the amount is greater than any of the valid denominations
    # Subtract the denomination and increase notes by 1
    if amt>=2000:
        amt-=2000
        notes+=1
    elif amt>=1000:
        amt-=1000
        notes+=1
    elif amt>=500:
        amt-=500
        notes+=1
    elif amt>=200:
        amt-=200
        notes+=1
    elif amt>=100:
        amt-=100
        notes+=1
    elif amt>=50:
        amt-=50
        notes+=1
    elif amt>=20:
        amt-=20
        notes+=1
    elif amt>=10:
        amt-=10
        notes+=1
    else:
        # If the amount is no longer deductible, print the amount
        # As it is present only in coins
        print('Amount present in coins', amt)
        break

print('Number of notes present in the amount is',notes)
