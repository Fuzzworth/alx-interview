#!/usr/bin/python3
"""
Module Docs
"""
from typing import List

START_BYTE_MASK = 0b1110
CONTINUATION_BYTE_MASK = 0b110


def validUTF8(data: List[int]) -> bool:
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data (List[int]): List of integers representing 1-byte data.
    Each integer represents 8 least significant bits.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else return False.
    """

    # Variable to track the number of expected continuation bytes
    expected_continuations = 0

    for byte in data:
        if expected_continuations == 0:
            # Check if the current byte is a start byte
            if (byte & START_BYTE_MASK) == 0b110:
                expected_continuations = 1
            elif (byte & CONTINUATION_BYTE_MASK) == 0b1110:
                expected_continuations = 2
            elif (byte & CONTINUATION_BYTE_MASK) == 0b11110:
                expected_continuations = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the current byte is a continuation byte
            if (byte & CONTINUATION_BYTE_MASK) != 0b10:
                return False
            expected_continuations -= 1

    return expected_continuations == 0
