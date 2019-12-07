import unittest
import numpy as np
import random
from iv_jett import iv_init

class TestBetas(unittest.TestCase):
    def test_square_instruments(self):
        z = np.random.rand(255, 5)
        x = np.random.rand(255, 5)
        y = np.random.rand(255, 5)

        betas = np.linalg.inv(np.transpose(z) @ x) @ np.transpose(z) @ y
        x2 = iv_init.estimate_beta_iv(x, z, y, nocons = True)

        self.assertIsNone(np.testing.assert_allclose(betas, x2))

    def test_large_data(self):
        z = np.random.rand(10^8, 2)
        x = np.random.rand(10^8, 2)
        y = np.random.rand(10^8, 2)

        betas = np.linalg.inv(np.transpose(z) @ x) @ np.transpose(z) @ y
        x2 = iv_init.estimate_beta_iv(x, z, y, nocons = True)

        self.assertIsNone(np.testing.assert_allclose(betas, x2))

    def test_nonsingular_x(self):
        random.seed(12345)
        colin_row = np.random.rand(1, 3)
        noncolin_row = np.random.rand(1, 3)
        collinear = np.transpose(np.stack((colin_row, 2* colin_row, noncolin_row ), axis = 0))

        mat_x  = collinear
        mat_z  = np.transpose(np.matrix([[1, .5, 2],
                    [3, 0, .2],
                    [1, 0, .4]]))

        mat_y  = np.transpose(np.array([[3, 5, 2]]))

        self.assertRaises(Exception)

    def test_nonsingular_z(self):
        collinear = np.transpose(np.matrix([ [1, 2, 3],
                    [2, 4, 6],
                    [96, 78, 0]]))

        mat_z  = collinear
        mat_x  = np.transpose(np.matrix([[1, .5, 2],
                    [3, 0, .2],
                    [1, 0, .4]]))

        mat_y  = np.transpose(np.array([[3, 5, 2]]))

        self.assertRaises(Exception)

if __name__ == "__main__":
    unittest.main()
