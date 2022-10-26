# Python Program to Calculate the Area and Perimeter of Triangle and Circle

import math

# FOR TRIANGLE
a, b, c = float(input('Side A of ∆ - ')), float(
    input('Side B of ∆ - ')), float(input('Side C of ∆ - '))

# Perimeter of a triangle is the sum of its sides
perimeter= a+b+c

# We use Heron's formula to calculate the area
# Define s which is half of perimeter
s = perimeter/2

# Using Heron's formula, root(s(sxa)(sxb)(sxc))
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('Perimeter of the ∆ is', perimeter, 'units')
print('Area of the ∆ is', area, 'units^2')

# FOR CIRCLE
radius = float(input('Radius of the circle - '))

# Perimeter of a circle is 2πr
perimeter = 2*math.pi*radius

# Area of a circle is πr^2
area = math.pi*math.pow(radius,2)

print('Perimeter of the Circle is', perimeter, 'units')
print('Area of the Circle is', area, 'units^2')
