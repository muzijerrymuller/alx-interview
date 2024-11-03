#!/usr/bin/python3
"""
UTF-8 Validation Module
This module provides a function to validate whether a given list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    UTF-8 encoding can represent a character in
    1 to 4 bytes. For a valid UTF-8 encoding:
    - A 1-byte character starts with a 0 bit at the
    most significant position (0xxxxxxx).
    - A 2-byte character starts with '110' and is followed
    by one continuation byte starting with '10'.
    - A 3-byte character starts with '1110' and is followed by
    two continuation bytes starting with '10'.
    - A 4-byte character starts with '11110' and is followed by
    three continuation bytes starting with '10'.
    Parameters:
    data (list): List of integers, where each integer
    represents one byte (8 bits).
    Returns:
    bool: True if data represents a valid UTF-8 encoding, False otherwise.
    Process:
    - The function iterates over each integer in the list,
    checking for a valid start byte or continuation byte.
    - It uses bitwise operations to count the number
    of expected continuation bytes.
    - If the pattern does not match a valid UTF-8
    encoding format, it returns False.
    Example:
    >>> validUTF8([197, 130, 1])
    True
    >>> validUTF8([235, 140, 4])
    False
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        mask_byte = 1 << 7

        if number_bytes == 0:
            while mask_byte & byte:
                number_bytes += 1
                mask_byte >>= 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        number_bytes -= 1

    return number_bytes == 0
