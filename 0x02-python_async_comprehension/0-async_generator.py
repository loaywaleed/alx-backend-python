#!/usr/bin/env python3
"""
Module that uses async generator
"""
import typing
import asyncio
import random


async def async_generator():
    """async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
