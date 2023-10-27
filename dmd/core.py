import numpy as np

def dmd(X, rank):
    """
    Perform Dynamic Mode Decomposition.
    
    Parameters:
    X (ndarray): The input data matrix where each column is a snapshot.
    rank (int): The rank for the truncation.
    
    Returns:
    Phi (ndarray): The dynamic modes.
    Lambda (ndarray): The eigenvalues.
    b (ndarray): The amplitudes.
    """
    X1, X2 = prepare_data(X)
    Ur, Sigma_r_inv, Vr = compute_svd(X1, rank)
    A_tilde = reduced_order_rep(Ur, X2, Vr, Sigma_r_inv)
    Lambda, W = eigen_decomposition(A_tilde)
    Phi = compute_dynamic_modes(X2, Vr, Sigma_r_inv, W)
    b = compute_amplitudes(Phi, X[:, 0])
    return Phi, Lambda, b

def prepare_data(X):
    """ Prepare the data matrices for DMD. """
    return X[:, :-1], X[:, 1:]

def compute_svd(X, rank):
    """ Compute the truncated SVD of a matrix. """
    U, Sigma, Vh = np.linalg.svd(X, full_matrices=False)
    return U[:, :rank], np.diag(1. / Sigma[:rank]), Vh.conj().T[:, :rank]

def reduced_order_rep(Ur, X2, Vr, Sigma_r_inv):
    """ Compute the reduced order representation. """
    return Ur.conj().T @ X2 @ Vr @ Sigma_r_inv

def eigen_decomposition(A):
    """ Perform eigen decomposition. """
    return np.linalg.eig(A)

def compute_dynamic_modes(X2, Vr, Sigma_r_inv, W):
    """ Compute the dynamic modes. """
    return X2 @ Vr @ Sigma_r_inv @ W

def compute_amplitudes(Phi, X0):
    """ Compute the amplitudes for the modes. """
    return np.linalg.lstsq(Phi, X0, rcond=None)[0]

