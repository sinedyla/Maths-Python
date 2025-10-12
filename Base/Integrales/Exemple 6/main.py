from sympy import *

x = symbols('x')

f = 2*x + 1

aire = integrate(f,(x, 0, 1))

print(aire)