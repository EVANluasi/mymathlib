# optimization.py
import numpy as np

def gradient_descent(func, grad, start, lr=0.01, tol=1e-5, max_iter=1000):
    """
    Menyelesaikan masalah optimasi dengan metode gradient descent.
    
    Args:
    func (function): Fungsi yang akan diminimalkan
    grad (function): Fungsi gradien dari fungsi yang akan diminimalkan
    start (np.ndarray): Titik awal untuk pencarian solusi
    lr (float): Laju pembelajaran, default 0.01
    tol (float): Toleransi perubahan, default 1e-5
    max_iter (int): Batas iterasi, default 1000
    
    Returns:
    np.ndarray: Solusi yang ditemukan
    """
    x = np.array(start)
    for _ in range(max_iter):
        grad_val = grad(x)
        x_new = x - lr * grad_val
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Contoh fungsi dan gradiennya
def func(x):
    return x[0]**2 + x[1]**2  # f(x, y) = x^2 + y^2

def grad(x):
    return np.array([2*x[0], 2*x[1]])  # grad f(x, y) = [2x, 2y]
