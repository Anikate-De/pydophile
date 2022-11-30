# Program to print all Prime numbers between 1 to n

n = int(input('Enter the value of n = '))
for num in range(1, n+1):
    for i in range(2, num // 2):
        if num % i == 0:
            break
    else:
        print(num)
