import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dmd.core import dmd
from dmd.utils import reconstruct_dynamics, plot_dynamics

def generate_sho_data(omega, t_end, n_points):
    """
    Generate data for a simple harmonic oscillator.

    Parameters:
    omega (float): Angular frequency of the oscillator.
    t_end (float): End time for the data.
    n_points (int): Number of data points.

    Returns:
    ndarray: Data matrix for the simple harmonic oscillator.
    """
    t = np.linspace(0, t_end, n_points)
    data = np.array([np.sin(omega * t), np.cos(omega * t)])
    return data

def sho_hamiltonian(q, p):
    """
    Compute the Hamiltonian of a simple harmonic oscillator.

    Parameters:
    q, p (ndarray): Position and momentum.

    Returns:
    ndarray: Hamiltonian values.
    """
    return 0.5 * (p**2 + q**2)

def plot_phase_portrait(data, title="Phase Portrait"):
    """
    Plot the phase portrait of the dynamics.

    Parameters:
    data (ndarray): Data matrix where the first row is position and second row is momentum.
    title (str): Title of the plot.
    """
    plt.figure()
    plt.plot(data[0], data[1], 'r-', label='Trajectory')
    plt.scatter(data[0, 0], data[1, 0], color='black', label='Start')
    plt.xlabel('Position (q)')
    plt.ylabel('Momentum (p)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def animate_dynamics(X, X_dmd, t_end):
    """
    Create an animation to show the original and reconstructed dynamics.

    Parameters:
    X, X_dmd (ndarray): Original and reconstructed data matrices.
    t_end (float): End time for the data.
    """
    fig, ax = plt.subplots()
    line1, = ax.plot([], [], 'r-', label='Original')
    line2, = ax.plot([], [], 'b-', label='Reconstructed')

    def init():
        ax.set_xlim(np.min(X[0]), np.max(X[0]))
        ax.set_ylim(np.min(X[1]), np.max(X[1]))
        ax.set_xlabel('Position (q)')
        ax.set_ylabel('Momentum (p)')
        ax.set_title('Dynamics Animation')
        ax.legend()
        ax.grid(True)
        return line1, line2

    def update(frame):
        line1.set_data(X[0, :frame], X[1, :frame])
        line2.set_data(X_dmd[0, :frame], X_dmd[1, :frame])
        return line1, line2

    ani = FuncAnimation(fig, update, frames=np.linspace(0, X.shape[1], 200, dtype=int), init_func=init, blit=True, interval=50)
    plt.show()

def main():
    # Set parameters
    omega = 2.0 * np.pi  # Angular frequency
    t_end = 10          # End time
    n_points = 1000     # Number of data points
    rank = 2            # Rank for DMD

    # Generate data
    X = generate_sho_data(omega, t_end, n_points)

    # Apply DMD
    Phi, Lambda, b = dmd(X, rank)

    # Reconstruct dynamics
    steps = X.shape[1]
    X_dmd = reconstruct_dynamics(Phi, Lambda, b, steps)

    # Plot original vs reconstructed dynamics
    plot_dynamics(X, X_dmd)

    # Phase-plane portrait of original dynamics
    plot_phase_portrait(X, title="Original Phase Portrait")

    # Phase-plane portrait of reconstructed dynamics
    plot_phase_portrait(X_dmd, title="DMD Reconstructed Phase Portrait")

    # Compare Hamiltonian flow
    H_original = sho_hamiltonian(X[0], X[1])
    H_dmd = sho_hamiltonian(X_dmd[0], X_dmd[1])

    plt.figure()
    plt.plot(np.linspace(0, t_end, n_points), H_original, label='Original Hamiltonian')
    plt.plot(np.linspace(0, t_end, n_points), H_dmd, label='DMD Reconstructed Hamiltonian')
    plt.xlabel('Time')
    plt.ylabel('Hamiltonian')
    plt.title('Hamiltonian Flow')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

