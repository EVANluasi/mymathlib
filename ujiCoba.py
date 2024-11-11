# UJi Coba library buatan sendiri
import mymathlib
import numpy as np

# Matriks A dan B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matriks perkalian
C = mymathlib.matrix_multiply(A, B)
print("Matriks A * B:")
print(C)

# Determinan A
det_A = mymathlib.determinant(A)
print("Determinant A:", det_A)

# Invers A
try:
    inv_A = mymathlib.inverse(A)
    print("Invers A:")
    print(inv_A)
except ValueError as e:
    print(e)

# Eigenvalues dan eigenvectors
eigvals, eigvecs = mymathlib.eigen(A)
print("Eigenvalues A:", eigvals)
print("Eigenvectors A:")
print(eigvecs)
