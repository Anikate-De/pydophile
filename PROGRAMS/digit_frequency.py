# Program to find frequency of each digit in a given integer

number = int(input('Enter the number - '))

digitFrequency = {}

while number > 0:
    digit = number % 10
    if digit in digitFrequency:
        digitFrequency[digit] += 1
    else:
        digitFrequency[digit] = 1
    number //= 10

print('Digit', '-', 'Frequency')
for key, value in digitFrequency.items():
    print(key, '-', value)
