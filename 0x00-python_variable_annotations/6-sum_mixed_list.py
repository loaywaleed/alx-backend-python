#!/usr/bin/env python3
"""
Script that uses complex types
"""
from Typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function that returns sum of items in a list"""
    return sum(mxd_list)
