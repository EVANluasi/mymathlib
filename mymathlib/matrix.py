# matrix.py
import numpy as np

def matrix_multiply(A, B):
    """
    Mengalikan dua matriks A dan B.
    
    Args:
    A (list of list): Matriks pertama
    B (list of list): Matriks kedua
    
    Returns:
    list of list: Matriks hasil perkalian
    """
    return np.dot(A, B).tolist()

def determinant(matrix):
    """
    Menghitung determinan dari matriks.
    
    Args:
    matrix (list of list): Matriks yang akan dihitung determinannya
    
    Returns:
    float: Nilai determinan
    """
    return np.linalg.det(matrix)
