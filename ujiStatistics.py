import numpy as np
import mymathlib.statistics as stats
from scipy import stats as sp_stats

np.random.seed(42)
data_x = np.linspace(1, 100, 500)  
data_y_linear = data_x * 2 + np.random.normal(0, 5, 500)  
data_y_nonlinear = data_x**2 + np.random.normal(0, 25, 500)  
data_y_random = np.random.uniform(0, 10000, 500) 

# ----- Uji Coba Fungsi Dasar Statistik -----
print("----- Uji Coba Fungsi Dasar Statistik -----")
print(f"Mean dari X: {stats.mean(data_x)}")
print(f"Variance dari X: {stats.variance(data_x)}")
print(f"Standar Deviasi dari X: {stats.std_deviation(data_x)}")

print("\nMean dari Y Linear: ", stats.mean(data_y_linear))
print("Variance dari Y Linear: ", stats.variance(data_y_linear))
print("Standar Deviasi dari Y Linear: ", stats.std_deviation(data_y_linear))

print("\nMean dari Y Non-linear: ", stats.mean(data_y_nonlinear))
print("Variance dari Y Non-linear: ", stats.variance(data_y_nonlinear))
print("Standar Deviasi dari Y Non-linear: ", stats.std_deviation(data_y_nonlinear))

# ----- Korelasi Pearson dan Spearman antara Data X dan Data Y -----
print("\n----- Korelasi Pearson dan Spearman -----")
pearson_corr_linear = stats.correlation(data_x, data_y_linear)
spearman_corr_linear, _ = sp_stats.spearmanr(data_x, data_y_linear)

pearson_corr_nonlinear = stats.correlation(data_x, data_y_nonlinear)
spearman_corr_nonlinear, _ = sp_stats.spearmanr(data_x, data_y_nonlinear)

pearson_corr_random = stats.correlation(data_x, data_y_random)
spearman_corr_random, _ = sp_stats.spearmanr(data_x, data_y_random)

print(f"Korelasi Pearson (Linear): {pearson_corr_linear}")
print(f"Korelasi Spearman (Linear): {spearman_corr_linear}")

print(f"Korelasi Pearson (Non-linear): {pearson_corr_nonlinear}")
print(f"Korelasi Spearman (Non-linear): {spearman_corr_nonlinear}")

print(f"Korelasi Pearson (Random): {pearson_corr_random}")
print(f"Korelasi Spearman (Random): {spearman_corr_random}")

# ----- Uji Coba Regresi Linear dan Non-linear -----
print("\n----- Regresi Linear dan Non-linear -----")
linear_slope, linear_intercept = stats.linear_regression(data_x, data_y_linear)
print(f"Regresi Linear (Linear): Y = {linear_slope} * X + {linear_intercept}")

coeffs_nonlinear = np.polyfit(data_x, data_y_nonlinear, 2)
print(f"Regresi Non-linear (Polynomial Fit): Y = {coeffs_nonlinear[0]} * X^2 + {coeffs_nonlinear[1]} * X + {coeffs_nonlinear[2]}")

# ----- Prediksi dengan Regresi Linear dan Non-linear -----
print("\n----- Prediksi dengan Model -----")
x_new = np.array([110, 120, 130, 140, 150])

y_pred_linear = linear_slope * x_new + linear_intercept
print(f"Prediksi Y (Linear) untuk X baru: {y_pred_linear}")

y_pred_nonlinear = coeffs_nonlinear[0] * x_new**2 + coeffs_nonlinear[1] * x_new + coeffs_nonlinear[2]
print(f"Prediksi Y (Non-linear) untuk X baru: {y_pred_nonlinear}")

# ----- Eksplorasi Dataset Yang Lebih Besar (Large Cardinal) -----
print("\n----- Eksplorasi dengan Large Cardinal -----")
large_data_x = np.random.randint(1, 1e7, size=int(1e5))
large_data_y = 3 * large_data_x + np.random.normal(0, 100, size=int(1e5)) 

print(f"Mean dari large_data_x: {stats.mean(large_data_x)}")
print(f"Variance dari large_data_y: {stats.variance(large_data_y)}")

large_correlation = stats.correlation(large_data_x, large_data_y)
print(f"Korelasi Pearson pada dataset besar: {large_correlation}")

large_slope, large_intercept = stats.linear_regression(large_data_x, large_data_y)
print(f"Regresi Linear pada dataset besar Y = {large_slope} * X + {large_intercept}")
