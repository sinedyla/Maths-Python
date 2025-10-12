from sympy import *

x = symbols('x')
f = x ** 5 + x ** 3 + 7
df_x = diff(f)

print(df_x.subs(x,0))