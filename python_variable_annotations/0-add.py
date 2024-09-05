#!/usr/bin/env python3
"""
A script for a type-annotated function `add` that
takes a float `a` and a float `b` as arguments
and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """Adds two floats and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of `a` and `b`.
    """
    return a + b
