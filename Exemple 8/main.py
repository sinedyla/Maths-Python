from sympy import *

x = symbols('x')
f = 1/x
limite = limit(f,x,oo)

print(limite)