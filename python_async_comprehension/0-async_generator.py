#!/usr/bin/env python3
"""
Module 0-async_generator
Contains an asynchronous generator that yields random numbers
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random numbers.

    Loops 10 times, each time waits 1 second asynchronously,
    then yields a random float between 0 and 10.

    Yields:
        A random float between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
