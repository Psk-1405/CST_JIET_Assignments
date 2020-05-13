import math
a=int(input("Enter the Number of Square Blocks:- "))
ans=(math.sqrt(1+8*a)-1)/2 # Derived from AP formulae and Roots of quadratic Equations
print("Maximum Height of staircase:- {0:d}".format(math.floor(ans)))