#!/usr/bin/env python3
"""
Module 5-sum_list
Contains a function that returns the sum of a list of floats and ints
"""

from typing import List, Union

def sum_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats and ints
    Args:
        mixed_list: list of floats and ints
    Returns:
        The sum of the list
    """
    return sum(mixed_list)
