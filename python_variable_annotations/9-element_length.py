#!/usr/bin/env python3
"""
Module 9-element_length
Contains a function that returns a list of tuples
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    containing each element and its length.

    Args:
        lst: an iterable containing sequences (strings, lists, etc.)

    Returns:
        A list of tuples (element, length)
    """
    return [(i, len(i)) for i in lst]
