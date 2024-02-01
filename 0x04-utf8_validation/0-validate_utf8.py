#!/usr/bin/python3
"""
Module Docs
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data (list of int): List of integers representing 1-byte data.
    Each integer represents 8 least significant bits.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else return False.
    """

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        # Count the number of consecutive set bits starting from the most significant bit
        num_bytes = 0
        mask = 1 << 7
        while mask & data[i]:
            num_bytes += 1
            mask >>= 1

        # Validate the number of bytes based on the rules for UTF-8 encoding
        if num_bytes == 1 or num_bytes > 4:
            return False

        # Check that the following bytes are valid continuations
        for j in range(1, num_bytes):
            if i + j >= len(data) or (data[i + j] >> 6) != 0b10:
                return False

        i += num_bytes

    return True
