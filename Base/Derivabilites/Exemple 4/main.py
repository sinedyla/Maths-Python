from sympy import *

x, y = symbols('x y')

f = 4*x**2 + 3*x*y**2 + y

df_x = diff(f,x)
df_y = diff(f,y)

print(df_x)
print(df_y)