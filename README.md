# Dynamic Mode Decomposition (DMD)

Dynamic Mode Decomposition (DMD) is a powerful analysis tool for capturing the essential features of complex and high-dimensional datasets, particularly time-series data. This Python package provides a straightforward and flexible implementation of DMD, suitable for a wide range of applications from fluid dynamics to financial modeling.

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Examples](#examples)
- [License](#license)
- [References](#references)

## Installation

To install the Dynamic Mode Decomposition package, you can clone the repository and install the dependencies with pip:

```bash
git clone https://github.com/joseph-crowley/dynamic-mode-decomposition.git
cd dynamic-mode-decomposition
pip install -r requirements.txt
```

## Quick Start

To use DMD in your project, simply import the `dmd` function from the `core` module:

```python
from dmd.core import dmd

# Your data matrix X
# X = ...

# Applying DMD with a specified rank
Phi, Lambda, b = dmd(X, rank=2)
```

## Documentation

Documentation is available in the `docs` folder. Start with `dmd_explained.md` for an explanation of the Dynamic Mode Decomposition algorithm and its applications.

## Examples

For practical examples, check out the `examples` directory. The `harmonic_oscillator.py` script demonstrates how to apply DMD to a simple harmonic oscillator system, including visualizations of the results and advanced analyses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- "Dynamic Mode Decomposition: Data-Driven Modeling of Complex Systems" by J. Nathan Kutz, Steven L. Brunton, Bingni W. Brunton, and Joshua L. Proctor. [link](http://dmdbook.com)

