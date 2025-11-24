#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Contains a function that returns the sum of a list of floats and ints
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats and ints
    Args:
        mxd_lst: list of floats and ints
    Returns:
        The sum of the list as a float
    """
    return sum(mxd_lst)
