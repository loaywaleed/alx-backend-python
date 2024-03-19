#!/usr/bin/env python3
""" Module that contains a function that returns an async task """
import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an async tast"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
