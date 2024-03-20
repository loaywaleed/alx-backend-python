#!/usr/bin/env python3
"""
Module that measures runtime of 4 async async_comprehension in parallel
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measuring runtime"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension() for _ in range(4))
    elapsed = time.perf_counter() - start
    return elapsed
