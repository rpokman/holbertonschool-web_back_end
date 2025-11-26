#!/usr/bin/env python3
"""
Module 0-basic_async_syntax
Contains an asynchronous coroutine that waits for a random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay: Maximum delay in seconds (default: 10)

    Returns:
        The random delay (float) that was waited
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
