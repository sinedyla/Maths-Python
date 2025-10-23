from numpy import *

X = [1,2,3]
Px = [0.2, 0.3, 0.5]

esperance = sum( x*p for x,p in zip(X,Px))

print(esperance)