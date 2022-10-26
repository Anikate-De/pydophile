# Python Program to Solve Quadratic Equations

import math

a, b, c = float(input('A - ')), float(input('B - ')), float(input('B - '))
discriminant = math.pow(b, 2) - 4 * a * c

if discriminant == 0:

    print('Two real & equal roots exist')
    print(-b/(2*a))
    print(-b/(2*a))

elif discriminant > 0:

    print('Two real & unique roots exist')
    print(-b + math.sqrt(discriminant) / (2*a))
    print(-b - math.sqrt(discriminant) / (2*a))

else:

    print('Two imaginary roots exist')
    comp = math.sqrt(-discriminant)
    print(complex(-b, comp) / (2*a))
    print(complex(-b, -comp) / (2*a))
