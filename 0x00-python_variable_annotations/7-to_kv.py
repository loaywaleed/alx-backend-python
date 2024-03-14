#!/usr/bin/env python3
"""
Script that uses complex annotation types
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple of a string and square of the 2nd arg"""
    return k, float(v ** 2)
