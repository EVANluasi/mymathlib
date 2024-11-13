import unittest
import math
import mymathlib.trigonometry as trig

class TestTrigonometry(unittest.TestCase):
    
    def test_sin(self):
        self.assertAlmostEqual(trig.sin(math.pi / 2), 1.0, places=5)

    def test_cos(self):
        self.assertAlmostEqual(trig.cos(0), 1.0, places=5)

    def test_tan(self):
        self.assertAlmostEqual(trig.tan(math.pi / 4), 1.0, places=5)

    def test_sec(self):
        self.assertAlmostEqual(trig.sec(0), 1.0, places=5)

    def test_csc(self):
        self.assertAlmostEqual(trig.csc(math.pi / 2), 1.0, places=5)

    def test_cot(self):
        self.assertAlmostEqual(trig.cot(math.pi / 4), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
