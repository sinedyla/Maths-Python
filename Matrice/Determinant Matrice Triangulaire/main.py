from numpy import *

A = array([[1,2,3],[0,3,4],[0,0,6]])

produit = prod(diag(A))

print(produit)