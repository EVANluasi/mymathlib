import numpy as np
import mymathlib  

# ------------------- Uji Coba 1: Persamaan Linear Sederhana (ax + b = 0) -------------------
print("----- Uji Coba: Persamaan Linear Sederhana -----")
# Persamaan: 2x + 3 = 0
a = 2
b = -3

solusi_linear = mymathlib.solve_linear(a, b)
print(f"Solusi untuk persamaan {a}x + {b} = 0 adalah x = {solusi_linear}")

# ------------------- Uji Coba 2: Sistem Persamaan Linear (AX = B) -------------------
print("\n----- Uji Coba: Sistem Persamaan Linear -----")
# Sistem persamaan:
# 2x + 3y = 5
# 4x - y = 6
A = np.array([[2, 3], [4, -1]]) 
B = np.array([5, 6]) 

# Menyelesaikan sistem AX = B
solusi_sistem = mymathlib.solve_linear_system(A, B)
print(f"Solusi sistem persamaan AX = B adalah: {solusi_sistem}")

# ------------------- Uji Coba 3: Matriks Invers dan Determinan -------------------
print("\n----- Uji Coba: Matriks Invers dan Determinan -----")
# Matriks A:
A_inv = np.array([[4, 7], [2, 6]])

# Menghitung determinan dan invers
det_A = mymathlib.determinant(A_inv)
A_inv_sol = mymathlib.inverse(A_inv)

print(f"Determinan dari A adalah: {det_A}")
print(f"Invers dari A adalah: \n{A_inv_sol}")

# ------------------- Uji Coba 4: Derivatif dan Integral -------------------
print("\n----- Uji Coba: Derivatif dan Integral -----")
# Fungsi f(x) = x^2
def f(x):
    return x**2

# Menghitung turunan (derivatif) dan integral
deriv = mymathlib.derivative(f, 2)  # Turunan pada x = 2
integral = mymathlib.integral(f, 0, 1)  # Integral dari x^2 antara 0 dan 1

print(f"Turunan dari f(x) = x^2 di x = 2 adalah: {deriv}")
print(f"Integral dari f(x) = x^2 antara 0 dan 1 adalah: {integral}")

# ------------------- Uji Coba 5: Optimasi (Gradient Descent) -------------------
print("\n----- Uji Coba: Optimasi (Gradient Descent) -----")
# Fungsi f(x) = x^2 - 4x + 4
def func(x):
    return x**2 - 4*x + 4

# Gradien fungsi
def grad_func(x):
    return 2*x - 4

# Menyelesaikan dengan Gradient Descent
initial_guess = 0  # Tebakan awal
learning_rate = 0.1
iterations = 100

optimum = mymathlib.gradient_descent(func, grad_func, initial_guess, learning_rate, iterations)
print(f"Nilai minimum fungsi ditemukan pada x = {optimum}")

# ------------------- Uji Coba 6: Statistik (Mean, Variance, Std, Regression) -------------------
print("\n----- Uji Coba: Statistik -----")
data = np.array([2, 4, 6, 8, 10])

mean_value = mymathlib.mean(data)
variance_value = mymathlib.variance(data)
std_deviation_value = mymathlib.std_deviation(data)

print(f"Mean: {mean_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_deviation_value}")

# ------------------- Uji Coba 7: Trigonometri -------------------
print("\n----- Uji Coba: Trigonometri -----")
angle_rad = np.pi / 4  # Sudut 45 derajat dalam radian

sin_value = mymathlib.sin(angle_rad)
cos_value = mymathlib.cos(angle_rad)
tan_value = mymathlib.tan(angle_rad)

print(f"sin(45°) = {sin_value}")
print(f"cos(45°) = {cos_value}")
print(f"tan(45°) = {tan_value}")
