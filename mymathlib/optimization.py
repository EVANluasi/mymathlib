import numpy as np

def numerical_gradient(func, x, epsilon=1e-8):
    """
    Menghitung gradien dari fungsi 'func' pada titik 'x' menggunakan metode perbedaan hingga.
    
    Args:
    func (function): Fungsi yang akan dihitung gradiennya
    x (np.ndarray): Titik di mana gradien dihitung
    epsilon (float): Nilai kecil untuk perbedaan hingga, default 1e-8
    
    Returns:
    np.ndarray: Gradien dari fungsi pada titik x
    """
    grad = np.zeros_like(x, dtype=float)
    for i in range(len(x)):
        x_eps = np.copy(x)
        x_eps[i] += epsilon
        f_x_eps = func(x_eps)
        f_x = func(x)
        grad[i] = (f_x_eps - f_x) / epsilon
    return grad

def gradient_descent(func, grad=None, start=[0, 0], lr=0.01, tol=1e-5, max_iter=1000):
    """
    Menyelesaikan masalah optimasi dengan metode gradient descent.
    
    Args:
    func (function): Fungsi yang akan diminimalkan
    grad (function or None): Fungsi gradien dari fungsi yang akan diminimalkan (opsional).
                             Jika None, gradien akan dihitung secara numerik.
    start (np.ndarray): Titik awal untuk pencarian solusi
    lr (float): Laju pembelajaran, default 0.01
    tol (float): Toleransi perubahan, default 1e-5
    max_iter (int): Batas iterasi, default 1000
    
    Returns:
    np.ndarray: Solusi yang ditemukan
    """
    x = np.array(start, dtype=float)
    
    for _ in range(max_iter):
        # Hitung gradien secara numerik jika gradien eksplisit tidak disediakan
        grad_val = grad(x) if grad is not None else numerical_gradient(func, x)
        
        # Update posisi
        x_new = x - lr * grad_val
        
        # Jika perubahan kurang dari toleransi, konvergensi tercapai
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Contoh fungsi tanpa gradien eksplisit
def func(x):
    return x[0]**2 + x[1]**2  # f(x, y) = x^2 + y^2
