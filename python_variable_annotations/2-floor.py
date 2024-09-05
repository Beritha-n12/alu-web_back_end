#!/usr/bin/env python3
"""
A script for a type-annotated function `floor` which takes
a float `n` as an argument and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """Returns the floor of a float.

    Args:
        n (float): The number to floor.

    Returns:
        int: The floor of `n`.
    """
    return math.floor(n)
