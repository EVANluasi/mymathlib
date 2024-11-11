# algebra.py

def add(a, b):
    """
    Fungsi untuk menambahkan dua bilangan.
    
    Args:
    a (float): Angka pertama
    b (float): Angka kedua
    
    Returns:
    float: Hasil penjumlahan
    """
    return a + b

def subtract(a, b):
    """
    Fungsi untuk mengurangi dua bilangan.
    
    Args:
    a (float): Angka pertama
    b (float): Angka kedua
    
    Returns:
    float: Hasil pengurangan
    """
    return a - b

def multiply(a, b):
    """
    Fungsi untuk mengalikan dua bilangan.
    
    Args:
    a (float): Angka pertama
    b (float): Angka kedua
    
    Returns:
    float: Hasil perkalian
    """
    return a * b

def divide(a, b):
    """
    Fungsi untuk membagi dua bilangan.
    
    Args:
    a (float): Angka pertama
    b (float): Angka kedua
    
    Returns:
    float: Hasil pembagian
    Raises:
    ValueError: Jika b == 0
    """
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol.")
    return a / b

def solve_linear(a, b):
    """
    Fungsi untuk menyelesaikan persamaan linear ax + b = 0.
    
    Args:
    a (float): Koefisien dari x
    b (float): Konstanta
    
    Returns:
    float: Nilai x yang menyelesaikan persamaan
    """
    if a == 0:
        raise ValueError("a tidak boleh nol untuk persamaan linear.")
    return -b / a
