from numpy import *

X = [1,2,3]
Px = [0.2, 0.3, 0.5]

esperance = sum(x*p for x,p in zip(X,Px))

esperance_carre = sum(x**2 * p for x,p in zip(X,Px))

variance = esperance_carre - (esperance)**2
print(variance)