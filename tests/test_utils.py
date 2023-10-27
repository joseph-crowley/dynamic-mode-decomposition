import unittest
import numpy as np
from dmd.utils import reconstruct_dynamics
from dmd.core import dmd

class TestUtilsFunctions(unittest.TestCase):

    def test_reconstruct_dynamics(self):
        # Generate synthetic data
        t = np.linspace(0, 2 * np.pi, 100)
        X = np.vstack([np.sin(t), np.cos(t)])

        # Perform DMD
        rank = 2
        Phi, Lambda, b = dmd(X, rank)

        # Reconstruct dynamics
        X_dmd = reconstruct_dynamics(Phi, Lambda, b, X.shape[1])

        # Check if reconstruction is close to the original
        np.testing.assert_array_almost_equal(X, X_dmd, decimal=2)

if __name__ == '__main__':
    unittest.main()

