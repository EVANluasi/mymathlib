# complex.py
import cmath

def add_complex(c1, c2):
    """
    Menambahkan dua bilangan kompleks.
    
    Args:
    c1 (complex): Bilangan kompleks pertama
    c2 (complex): Bilangan kompleks kedua
    
    Returns:
    complex: Hasil penjumlahan dua bilangan kompleks
    """
    return c1 + c2

def multiply_complex(c1, c2):
    """
    Mengalikan dua bilangan kompleks.
    
    Args:
    c1 (complex): Bilangan kompleks pertama
    c2 (complex): Bilangan kompleks kedua
    
    Returns:
    complex: Hasil perkalian dua bilangan kompleks
    """
    return c1 * c2

def conjugate(c):
    """
    Menghitung konjugat dari bilangan kompleks.
    
    Args:
    c (complex): Bilangan kompleks
    
    Returns:
    complex: Konjugat dari bilangan kompleks
    """
    return cmath.conj(c)

def modulus(c):
    """
    Menghitung modulus dari bilangan kompleks.
    
    Args:
    c (complex): Bilangan kompleks
    
    Returns:
    float: Nilai modulus dari bilangan kompleks
    """
    return abs(c)
