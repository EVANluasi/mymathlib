# calculus.py
import math

def derivative(func, x, h=1e-5):
    """
    Menghitung turunan numerik dari fungsi pada titik x menggunakan metode beda terbatas.
    
    Args:
    func (function): Fungsi yang akan dihitung turunannya
    x (float): Titik di mana turunan dihitung
    h (float): Langkah perubahan x, default 1e-5
    
    Returns:
    float: Nilai turunan dari fungsi di titik x
    """
    return (func(x + h) - func(x)) / h

def integral(func, a, b, n=1000):
    """
    Menghitung integral numerik menggunakan metode trapezoidal.
    
    Args:
    func (function): Fungsi yang akan diintegralkan
    a (float): Batas bawah dari integral
    b (float): Batas atas dari integral
    n (int): Jumlah subinterval, default 1000
    
    Returns:
    float: Nilai integral dari fungsi pada interval [a, b]
    """
    h = (b - a) / n
    total_area = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        total_area += func(a + i * h)
    return total_area * h

def limit(func, x, direction='both', h=1e-5):
    """
    Menghitung limit numerik dari fungsi pada titik x.
    
    Args:
    func (function): Fungsi yang akan dihitung limitnya
    x (float): Titik di mana limit dihitung
    direction (str): 'both', 'right', atau 'left' untuk arah limit
    h (float): Langkah perubahan x, default 1e-5
    
    Returns:
    float: Nilai limit dari fungsi pada titik x
    """
    if direction == 'both':
        return (func(x + h) - func(x - h)) / (2 * h)
    elif direction == 'right':
        return (func(x + h) - func(x)) / h
    elif direction == 'left':
        return (func(x) - func(x - h)) / h
    else:
        raise ValueError("Direction harus 'both', 'right', atau 'left'.")
