#!/usr/bin/env python3
"""
Module 5-sum_list
Contains a function that returns the sum of a list of floats and ints
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats
    Args:
        input_list: list of floats
    Returns:
        The sum of the list
    """
    return sum(input_list)
