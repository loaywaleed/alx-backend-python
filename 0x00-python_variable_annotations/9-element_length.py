#!/usr/bin/env python3
"""
Script that uses duck typing
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> Tuple[str, int]:
    return [(i, len(i)) for i in lst]
