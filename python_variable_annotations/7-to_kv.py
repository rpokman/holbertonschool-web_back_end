#!/usr/bin/env python3
"""
Module 7-to_kv
Contains a function that converts a key and value to a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments.
    The first element of the tuple is the string k.
    The second element is the square of the int.
    """
    return (k, v * v)
