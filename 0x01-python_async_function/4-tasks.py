#!/usr/bin/env python3
"""
Module that executes multiple coroutines
"""
from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine that executes multiple coroutines"""
    lst = []
    for _ in range(n):
        lst.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*lst))
