# Dynamic Mode Decomposition (DMD) Explained

Dynamic Mode Decomposition (DMD) is a data-driven analysis technique that provides insights into the fundamental frequencies, growth/decay rates, and spatial coherence structures of complex systems. Rooted in fluid dynamics, DMD has broad applications in various fields of physics, particularly those involving temporal and spatial evolution of systems.

## Theoretical Background

At its core, DMD is an eigenvalue problem aimed at discerning the intrinsic dynamics of a system from time series data. From the perspective of classical dynamics, DMD can be viewed as a tool for revealing the spectrum of dynamical behavior—akin to identifying normal modes in a vibrating system but extended to non-linear and non-periodic systems.

### Connection to Fourier Analysis and Koopman Operator Theory

DMD can be thought of as a bridge between Fourier analysis and Koopman operator theory. Where Fourier analysis decomposes signals into frequency components, DMD extends this concept to spatio-temporal data, offering a decomposition into modes each associated with a specific frequency and growth/decay rate. The connection to Koopman operator theory comes from DMD's ability to approximate the Koopman operator, which is an infinite-dimensional linear operator capable of describing the full dynamics of a nonlinear system.

## Mathematical Formulation

Given a set of temporal data snapshots \( X = [x_1, x_2, ..., x_m] \), DMD seeks to find a matrix \( A \) that best approximates the dynamics in a least-squares sense: \( x_{i+1} \approx A x_i \). This approximation leads to the eigenvalue problem:

\[ A \Phi = \Phi \Lambda \]

where \( \Phi \) represents the DMD modes and \( \Lambda \) contains the corresponding eigenvalues. The eigenvalues offer insights into the growth rates and oscillatory behavior of each mode.

## Physical Interpretation

Each DMD mode can be interpreted as a spatial pattern whose intensity or presence in the physical system evolves according to the corresponding eigenvalue. For a physicist, this is akin to modal analysis in systems with multiple degrees of freedom, but DMD does not require the system to be linear or conservative.

### Example: Simple Harmonic Oscillator

In the context of a simple harmonic oscillator (SHO), DMD effectively identifies the characteristic frequency of oscillation. The resulting DMD modes correspond to the sinusoidal position and momentum oscillations, and the eigenvalues directly relate to the oscillator's angular frequency.
