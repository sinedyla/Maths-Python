from sympy import *

x = symbols('x')

f = (x**2 + 5)**3 + x

df_x = diff(f,x)

print(df_x)