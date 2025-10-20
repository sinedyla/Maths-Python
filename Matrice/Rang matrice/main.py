from numpy import *

A = array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

rang = linalg.matrix_rank(A)

print(rang)