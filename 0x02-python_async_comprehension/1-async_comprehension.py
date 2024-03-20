#!/usr/bin/env python3
"""
Module showcasing async comprehension
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async comprehension function"""
    result = [random async for random in async_generator()]
    return result
