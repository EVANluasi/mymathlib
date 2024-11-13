import unittest
import numpy as np
import mymathlib.optimization as opt

class TestOptimization(unittest.TestCase):
    
    def setUp(self):
        self.func = lambda x: (x - 3)**2

    def test_gradient_descent(self):
        optimal_x = opt.gradient_descent(self.func, start=[10], lr=0.1, tol=1e-5, max_iter=100)
        self.assertAlmostEqual(optimal_x[0], 3.0, places=2)

    def test_large_cardinal_optimization(self):
        large_data = np.random.normal(3, 1, 1000000)  
        self.func_large = lambda x: np.mean((large_data - x)**2)
        optimal_x_large = opt.gradient_descent(self.func_large, start=[10], lr=0.1, tol=1e-5, max_iter=200)
        self.assertAlmostEqual(optimal_x_large[0], 3.0, places=1)

if __name__ == '__main__':
    unittest.main()
