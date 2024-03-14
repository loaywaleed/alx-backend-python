#!/usr/bin/env python3
"""
Script that uses duck typing
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Using iterables and sequence"""
    return [(i, len(i)) for i in lst]
