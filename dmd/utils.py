import numpy as np
import matplotlib.pyplot as plt

def reconstruct_dynamics(Phi, Lambda, b, steps):
    """
    Reconstruct the dynamics using DMD modes and eigenvalues.
    
    Parameters:
    Phi (ndarray): The dynamic modes.
    Lambda (ndarray): The eigenvalues.
    b (ndarray): The amplitudes.
    steps (int): The number of time steps to reconstruct.
    
    Returns:
    X_dmd (ndarray): The reconstructed data matrix.
    """
    omega = np.log(Lambda)
    t = np.arange(steps)
    vander = np.exp(np.outer(omega, t))
    X_dmd = Phi @ np.diag(b) @ vander
    return X_dmd

def plot_dynamics(X, X_dmd):
    """
    Plot the original dynamics, approximated dynamics, and their differences.
    
    Parameters:
    X (ndarray): The original data matrix.
    X_dmd (ndarray): The reconstructed data matrix.
    """
    time_steps = X.shape[1]
    
    # Plot original dynamics
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.imshow(X.real, aspect='auto', extent=[0, time_steps, 0, X.shape[0]])
    plt.colorbar(label='Amplitude')
    plt.title('Original Dynamics')
    
    # Plot approximated dynamics
    plt.subplot(3, 1, 2)
    plt.imshow(X_dmd.real, aspect='auto', extent=[0, time_steps, 0, X_dmd.shape[0]])
    plt.colorbar(label='Amplitude')
    plt.title('Approximated Dynamics')
    
    # Plot difference
    plt.subplot(3, 1, 3)
    plt.imshow((X - X_dmd).real, aspect='auto', extent=[0, time_steps, 0, X.shape[0]])
    plt.colorbar(label='Amplitude')
    plt.title('Difference')
    
    plt.tight_layout()
    plt.show()

