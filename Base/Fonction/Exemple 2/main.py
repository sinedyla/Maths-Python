import sympy as sp
from sympy.plotting import plot

x = sp.symbols('x')
f = 2 * x**2 + 1

plot(f)