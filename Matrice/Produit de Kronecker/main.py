from numpy import *

A = array([[1,2],[3,4]])
B = array([[5,6],[7,8]])

produit_kron = kron(A,B)

print(produit_kron)