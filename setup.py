from setuptools import setup, find_packages

setup(
    name="DMD-Analysis",
    version="0.1.0",
    author="Joe Crowley",
    author_email="crowley@ucsb.edu",
    description="A Python package for Dynamic Mode Decomposition (DMD) analysis.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joseph-crowley/dynamic-mode-decomposition",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

