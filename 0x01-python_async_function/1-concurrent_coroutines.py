#!/usr/bin/env python3
"""
Module that executes multiple coroutines
"""
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine that executes multiple coroutines"""
    lst = []
    for _ in range(n):
        lst.append(wait_random(max_delay))
    return sorted(await asyncio.gather(*lst))
