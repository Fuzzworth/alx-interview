#!/usr/bin/python3
"""
Module Docs
"""
from typing import List


def min_operations_to_get_n_H_characters(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters in the file.

    Args:
    - n (int): The desired number of 'H' characters.

    Returns:
    - int: The fewest number of operations needed. If n is impossible to achieve, return 0.
    """
    if n <= 0:
        return 0

    # Initialize an array to store the minimum operations needed for each position
    min_operations = [float('inf')] * (n + 1)

    # Base case: It takes 0 operations to have 1 'H'
    min_operations[1] = 0

    for current_n in range(2, n + 1):
        # Try to find the minimum operations by checking all possible divisors
        for divisor in range(1, int(current_n**0.5) + 1):
            if current_n % divisor == 0:
                # Copy all and paste or paste divisor times
                min_operations[current_n] = min(
                    min_operations[current_n],
                    min_operations[divisor] + current_n // divisor,
                    min_operations[current_n // divisor] + divisor
                )

    return min_operations[n] if min_operations[n] != float('inf') else 0
