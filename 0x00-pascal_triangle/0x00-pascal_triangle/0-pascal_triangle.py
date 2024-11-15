#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Pascal's Triangle Generator

This module provides a function `pascal_triangle` to generate Pascal's Triangle 
up to a specified number of rows. Pascal's Triangle is a triangular array of 
the binomial coefficients, widely used in combinatorics, algebra, and geometry.

The triangle starts with a single 1 at the top, and each subsequent row is 
constructed using the principle that each number is the sum of the two directly 
above it. This implementation leverages mathematical formulas for efficiency.

Example:
    For n = 5, the Pascal's Triangle generated would be:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

Usage:
    Call the `pascal_triangle(n)` function with a positive integer `n` to get 
    a list of lists representing the triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    This function constructs Pascal's Triangle using a mathematical approach
    to compute each binomial coefficient for a given row. It returns a list
    of lists where each inner list represents a row of the triangle.
    Args:
        n (int): The number of rows in Pascal's Triangle to generate. Must be
        a non-negative integer.
    Returns:
        list: A list of lists containing the integers representing Pascal's
        Triangle. If n <= 0, returns an empty list.
    Example:
        >>> pascal_triangle(4)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    Notes:
        - Pascal's Triangle is widely used in mathematics and computer science,
          especially in binomial expansions and probability theory.
        - The computation of elements in each row uses integer division for
          efficiency and avoids floating-point arithmetic.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
