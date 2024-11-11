# trigonometry.py
import math

def sin(x):
    """
    Menghitung sinus dari x (dalam radian).
    
    Args:
    x (float): Sudut dalam radian
    
    Returns:
    float: Nilai sinus dari x
    """
    return math.sin(x)

def cos(x):
    """
    Menghitung cosinus dari x (dalam radian).
    
    Args:
    x (float): Sudut dalam radian
    
    Returns:
    float: Nilai cosinus dari x
    """
    return math.cos(x)

def tan(x):
    """
    Menghitung tangen dari x (dalam radian).
    
    Args:
    x (float): Sudut dalam radian
    
    Returns:
    float: Nilai tangen dari x
    """
    return math.tan(x)

def sec(x):
    """
    Menghitung sekans dari x (1/cos(x)).
    
    Args:
    x (float): Sudut dalam radian
    
    Returns:
    float: Nilai sekans dari x
    """
    return 1 / math.cos(x)

def csc(x):
    """
    Menghitung kosekans dari x (1/sin(x)).
    
    Args:
    x (float): Sudut dalam radian
    
    Returns:
    float: Nilai kosekans dari x
    """
    return 1 / math.sin(x)

def cot(x):
    """
    Menghitung kotangen dari x (1/tan(x)).
    
    Args:
    x (float): Sudut dalam radian
    
    Returns:
    float: Nilai kotangen dari x
    """
    return 1 / math.tan(x)
