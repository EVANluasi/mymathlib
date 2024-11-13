import mymathlib
import numpy as np
import math

# ----- Uji Coba: Operasi Aljabar -----
print("----- Uji Coba: Operasi Aljabar -----")
a, b = 10, 5
print(f"Penjumlahan {a} + {b} = {mymathlib.add(a, b)}")
print(f"Pengurangan {a} - {b} = {mymathlib.subtract(a, b)}")
print(f"Perkalian {a} * {b} = {mymathlib.multiply(a, b)}")
print(f"Pembagian {a} / {b} = {mymathlib.divide(a, b)}")

# ----- Uji Coba: Persamaan Linear -----
print("\n----- Uji Coba: Persamaan Linear -----")
A = np.array([[3, 2], [1, 2]])
B = np.array([16, 10])
try:
    solusi_sistem = mymathlib.solve_linear_system(A, B)
    print(f"Solusi untuk sistem persamaan AX = B adalah X = {solusi_sistem}")
except ValueError as e:
    print(f"Error: {e}")

# ----- Uji Coba: Kalkulus (Turunan dan Integral) -----
print("\n----- Uji Coba: Kalkulus (Turunan dan Integral) -----")
# Turunan dari f(x) = 3x^2 pada x = 2
print(f"Turunan dari f(x) = 3x^2 pada x = 2 adalah {mymathlib.derivative(lambda x: 3*x**2, 2)}")

# Integral dari f(x) = x^2 dari 0 hingga 3
print(f"Integral dari f(x) = x^2 dari 0 hingga 3 adalah {mymathlib.integral(lambda x: x**2, 0, 3)}")

# ----- Uji Coba: Statistik -----
print("\n----- Uji Coba: Statistik -----")
data = [4, 8, 6, 5, 3, 9, 7]
print(f"Mean dari data adalah {mymathlib.mean(data)}")
print(f"Varians dari data adalah {mymathlib.variance(data)}")
print(f"Standar deviasi dari data adalah {mymathlib.std_deviation(data)}")

# Korelasi antara dua dataset
data_x = [1, 2, 3, 4, 5]
data_y = [2, 4, 6, 8, 10]
print(f"Korelasi antara data_x dan data_y adalah {mymathlib.correlation(data_x, data_y)}")

# ----- Uji Coba: Trigonometri -----
print("\n----- Uji Coba: Trigonometri -----")
angle_rad = math.pi / 4  # 45 derajat dalam radian
print(f"sin({angle_rad}) = {mymathlib.sin(angle_rad)}")
print(f"cos({angle_rad}) = {mymathlib.cos(angle_rad)}")
print(f"tan({angle_rad}) = {mymathlib.tan(angle_rad)}")
print(f"sec({angle_rad}) = {mymathlib.sec(angle_rad)}")
print(f"csc({angle_rad}) = {mymathlib.csc(angle_rad)}")
print(f"cot({angle_rad}) = {mymathlib.cot(angle_rad)}")

# ----- Uji Coba: Optimasi -----
print("\n----- Uji Coba: Optimasi -----")
# Fungsi kuadrat sederhana f(x) = (x - 3)^2 yang minimum di x = 3
def f(x):
    return (x[0] - 3)**2  # Fungsi ini membutuhkan input array untuk gradient descent

start_point = np.array([10.0])  # Titik awal optimasi dalam bentuk array
learning_rate = 0.1
tolerance = 1e-5
num_iterations = 100

optimal_x = mymathlib.gradient_descent(func=f, start=start_point, lr=learning_rate, tol=tolerance, max_iter=num_iterations)
print(f"Nilai x yang meminimalkan fungsi f(x) = (x - 3)^2 adalah x = {optimal_x[0]}")
