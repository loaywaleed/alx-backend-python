#!/usr/bin/env python3
"""
Script that uses complex annotation types
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a tuple of a string and square of the 2nd arg"""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
