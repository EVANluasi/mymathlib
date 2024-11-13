import unittest
import numpy as np
import mymathlib.statistics as stats

class TestStatistics(unittest.TestCase):
    
    def setUp(self):
        self.data = [4, 8, 6, 5, 3, 9, 7]
        self.large_data = np.random.randint(1, 1e6, size=100000)
        self.x = np.array([1, 2, 3, 4, 5])
        self.y = np.array([2, 4, 6, 8, 10])  # Perfect linear correlation with x

    def test_mean(self):
        self.assertAlmostEqual(stats.mean(self.data), 6.0, places=1)

    def test_variance(self):
        self.assertAlmostEqual(stats.variance(self.data), 4.0, places=1)

    def test_std_deviation(self):
        self.assertAlmostEqual(stats.std_deviation(self.data), 2.0, places=1)

    def test_correlation_perfect(self):
        corr = stats.correlation(self.x, self.y)
        self.assertAlmostEqual(corr, 1.0, places=5)

    def test_large_data_statistics(self):
        # Ensure calculations complete without error on large dataset
        mean_large = stats.mean(self.large_data)
        variance_large = stats.variance(self.large_data)
        self.assertTrue(np.isscalar(mean_large) and np.isscalar(variance_large))

    def test_linear_regression(self):
        slope, intercept = stats.linear_regression(self.x, self.y)
        self.assertAlmostEqual(slope, 2.0, places=1)
        self.assertAlmostEqual(intercept, 0.0, places=1)

if __name__ == '__main__':
    unittest.main()
