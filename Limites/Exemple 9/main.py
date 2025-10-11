from sympy import *

x = symbols('x')
g = ((1+1/x))**x
limite = limit(g,x,oo)

print(limite)