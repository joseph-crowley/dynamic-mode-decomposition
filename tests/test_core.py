import unittest
import numpy as np
from dmd.core import dmd, prepare_data, compute_svd, reduced_order_rep, eigen_decomposition, compute_dynamic_modes, compute_amplitudes

class TestCoreFunctions(unittest.TestCase):

    def test_prepare_data(self):
        X = np.random.rand(5, 10)
        X1, X2 = prepare_data(X)
        self.assertEqual(X1.shape, (5, 9))
        self.assertEqual(X2.shape, (5, 9))
        np.testing.assert_array_almost_equal(X[:, :-1], X1)
        np.testing.assert_array_almost_equal(X[:, 1:], X2)

    def test_compute_svd(self):
        X = np.random.rand(5, 10)
        rank = 3
        U, S_inv, V = compute_svd(X, rank)
        self.assertEqual(U.shape, (5, rank))
        self.assertEqual(S_inv.shape, (rank, rank))
        self.assertEqual(V.shape, (10, rank))

    def test_reduced_order_rep(self):
        X1 = np.random.rand(5, 10)
        X2 = np.random.rand(5, 10)
        U, S_inv, V = compute_svd(X1, 3)
        A_tilde = reduced_order_rep(U, X2, V, S_inv)
        self.assertEqual(A_tilde.shape, (3, 3))

    def test_eigen_decomposition(self):
        A = np.random.rand(3, 3)
        Lambda, W = eigen_decomposition(A)
        self.assertEqual(Lambda.shape, (3,))
        self.assertEqual(W.shape, (3, 3))

    def test_compute_dynamic_modes(self):
        X2 = np.random.rand(5, 10)
        U, S_inv, V = compute_svd(X2, 3)
        A_tilde = reduced_order_rep(U, X2, V, S_inv)
        Lambda, W = eigen_decomposition(A_tilde)
        Phi = compute_dynamic_modes(X2, V, S_inv, W)
        self.assertEqual(Phi.shape, (5, 3))

    def test_compute_amplitudes(self):
        X = np.random.rand(5, 10)
        rank = 3
        Phi, Lambda, b = dmd(X, rank)
        self.assertEqual(b.shape, (3,))

if __name__ == '__main__':
    unittest.main()

