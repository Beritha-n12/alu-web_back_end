#!/usr/bin/env python3
"""
A script with a type-annotated function `concat`
that takes a string `str1` and a string `str2`
as arguments and returns a concatenated string.
"""


def concat(str1: str, str2: str) -> str:
    """Concatenates two strings and returns the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: A concatenated string.
    """
    return str1 + str2
