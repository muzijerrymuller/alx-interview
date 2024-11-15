#!/usr/bin/python3
"""Module for calculating the minimum number of
operations to achieve 'n' H characters.
This module contains a function, `minOperations`, which calculates the minimum
number of operations needed to result in exactly
'n' H characters, starting with
a single character 'H'. The operations allowed are 'Copy All' and 'Paste'.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    to result in exactly 'n' H characters.
    The operations available are 'Copy All'
    and 'Paste'. The function determines
    how many operations are required to
    reach 'n' H characters, starting from one
    'H'. If the number of characters is less
    than 2, the function returns 0,
    it is not possible to perform the necessary operations.
    Parameters:
    n (int): The number of H characters to be achieved.
    Must be a positive integer.
    Returns:
    int: The minimum number of operations required
    to achieve exactly 'n' H characters.Returns 0 if the operation
    is impossible (e.g., if n is less than 2)
    Example:
    >>> minOperations(9)
    6
    >>> minOperations(12)
    7
    """
    # If n is less than 2, it is not possible to perform any operations
    if n < 2:
        return 0
    o, r = 0, 2
    # Find factors of n that lead to minimum operations
    while r <= n:
        # Check if n is divisible by the current root
        if n % r == 0:
            # If divisible, add the factor to the operation count
            o += r
            # Update n to the quotient after division
            n = n / r
            # Reduce the root to find the next smallest factor
            r -= 1
        # Increment root to check for the next potential factor
        r += 1

    return o
