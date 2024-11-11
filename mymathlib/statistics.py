# statistics.py
import numpy as np
from scipy import stats

def mean(data):
    """
    Menghitung rata-rata dari data.
    
    Args:
    data (list or np.ndarray): Data yang akan dihitung rata-ratanya
    
    Returns:
    float: Nilai rata-rata
    """
    return np.mean(data)

def variance(data):
    """
    Menghitung varians dari data.
    
    Args:
    data (list or np.ndarray): Data yang akan dihitung variansinya
    
    Returns:
    float: Nilai variansi
    """
    return np.var(data)

def std_deviation(data):
    """
    Menghitung deviasi standar dari data.
    
    Args:
    data (list or np.ndarray): Data yang akan dihitung deviasi standarnya
    
    Returns:
    float: Nilai deviasi standar
    """
    return np.std(data)

def correlation(x, y):
    """
    Menghitung koefisien korelasi Pearson antara dua set data.
    
    Args:
    x (list or np.ndarray): Data pertama
    y (list or np.ndarray): Data kedua
    
    Returns:
    float: Nilai koefisien korelasi
    """
    return np.corrcoef(x, y)[0, 1]

def linear_regression(x, y):
    """
    Menyelesaikan regresi linear antara dua set data x dan y.
    
    Args:
    x (list or np.ndarray): Data independen
    y (list or np.ndarray): Data dependen
    
    Returns:
    tuple: Koefisien regresi (slope, intercept)
    """
    slope, intercept, _, _, _ = stats.linregress(x, y)
    return slope, intercept
