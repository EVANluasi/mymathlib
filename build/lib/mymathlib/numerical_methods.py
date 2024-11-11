# numerical_methods.py
import numpy as np

def newton_raphson(func, dfunc, x0, tol=1e-5, max_iter=100):
    """
    Menyelesaikan persamaan non-linear menggunakan metode Newton-Raphson.
    
    Args:
    func (function): Fungsi yang akan dicari akarnya
    dfunc (function): Turunan dari fungsi
    x0 (float): Tebakan awal untuk akar persamaan
    tol (float): Toleransi kesalahan, default 1e-5
    max_iter (int): Batas iterasi, default 100
    
    Returns:
    float: Akar dari persamaan
    """
    x = x0
    for _ in range(max_iter):
        x_new = x - func(x) / dfunc(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Tidak konvergen dalam jumlah iterasi maksimum.")

# Contoh fungsi dan turunannya
def func(x):
    return x**2 - 2  # f(x) = x^2 - 2

def dfunc(x):
    return 2 * x  # f'(x) = 2x
