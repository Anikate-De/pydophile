# A Program which will find all such numbers which are divisible by 7 but are not a multiple of 5
# Between 2000 and 3200 (both included)

for num in range(2000,3001):
    # Check for divisibility by 7 and indivisibility by 5
    if num%7 ==0 and not num%5==0:
        print(num)
