import numpy as np

def uniform(lo, hi):
    return np.random.uniform(lo, hi)

def randint(lo, hi):
    """Random integer, including 'hi'"""
    return np.random.randint(lo, hi + 1)

def randinte(lo, hi):
    """Random integer, excluding 'hi'"""
    return np.random.randint(lo, hi)
