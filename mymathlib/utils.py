# utils.py
def factorial(n):
    """
    Menghitung faktorial dari n (n!).
    
    Args:
    n (int): Bilangan yang akan dihitung faktorialnya
    
    Returns:
    int: Nilai faktorial dari n
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """
    Memeriksa apakah bilangan n adalah bilangan prima.
    
    Args:
    n (int): Bilangan yang akan diperiksa
    
    Returns:
    bool: True jika n adalah bilangan prima, False jika tidak
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
