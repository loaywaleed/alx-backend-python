#!/usr/bin/env python3
"""
Module that measures total execution time of aync coroutines
"""
import typing
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines", wait_n)


async def measure_time(n: int, max_delay: int) -> float:
    """Coroutine that calculates total execution time"""
    start_time: float = time.perf_counter()
    asyncio.run((wait_n(n, max_delay)))
    elapsed_time: float = time.perf_counter() - start_time
    return (elapsed_timed / n)
