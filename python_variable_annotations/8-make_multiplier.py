#!/usr/bin/env python3
"""
Module 8-make_multiplier
Contains a function that returns a multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies
    a float by the multiplier.

    Args:
        multiplier: the float to multiply by

    Returns:
        A function that takes a float and returns float * multiplier
    """
    def multiply(n: float) -> float:
        """Multiplies n by multiplier"""
        return n * multiplier

    return multiply
