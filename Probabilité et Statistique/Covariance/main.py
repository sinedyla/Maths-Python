from numpy import *

X = [1,2,3]
Y = [4,5,6]

P = [0.1,0.2,0.3]

Ex = sum(x*p for x,p in zip(X,P))

Ey = sum(y*p for y,p in zip(Y,P))

covariance = sum((x-Ex)*(y-Ey)*p for x,y,p in zip(X,Y,P))

print(covariance)