#!/usr/bin/env python3
"""
Module that has an async coroutine
"""
import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
