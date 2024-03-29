#!/usr/bin/env python3
"""
Module that has an async coroutine
"""
import asyncio
import random
import typing


async def wait_random(max_delay: int = 10) -> float:
    """coroutine that waits for a random duration"""
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
