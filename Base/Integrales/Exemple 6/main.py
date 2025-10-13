from sympy import *

x = symbols('x')
# Definition de la fonction
f = 2*x + 1

aire = integrate(f,(x, 0, 1))

print(aire)