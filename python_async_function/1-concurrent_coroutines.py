#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
Contains an async routine that spawns wait_random n times
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay for each wait_random call

    Returns:
        List of delays in ascending order (naturally, without sort)
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
