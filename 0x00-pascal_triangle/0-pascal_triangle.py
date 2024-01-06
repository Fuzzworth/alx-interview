#!/usr/bin/python3
"""
Module Docs
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    :param n: The number of rows to generate in Pascal's triangle.
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: List[List[int]]
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
