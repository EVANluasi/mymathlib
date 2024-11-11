# linear_algebra.py
import numpy as np

def matrix_multiply(A, B):
    """
    Mengalikan dua matriks A dan B.
    
    Args:
    A (np.ndarray): Matriks pertama
    B (np.ndarray): Matriks kedua
    
    Returns:
    np.ndarray: Matriks hasil perkalian
    """
    return np.dot(A, B)

def determinant(matrix):
    """
    Menghitung determinan dari matriks.
    
    Args:
    matrix (np.ndarray): Matriks yang akan dihitung determinannya
    
    Returns:
    float: Nilai determinan
    """
    return np.linalg.det(matrix)

def inverse(matrix):
    """
    Menghitung invers dari matriks, jika ada.
    
    Args:
    matrix (np.ndarray): Matriks yang akan dihitung inversnya
    
    Returns:
    np.ndarray: Matriks invers
    """
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Matriks tidak dapat dibalik (singular matrix).")

def eigen(matrix):
    """
    Menghitung eigenvalue dan eigenvector dari matriks.
    
    Args:
    matrix (np.ndarray): Matriks yang akan dihitung eigenvalue dan eigenvectornya
    
    Returns:
    tuple: Eigenvalues dan eigenvectors
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors
