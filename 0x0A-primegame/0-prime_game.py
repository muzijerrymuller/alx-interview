#!/usr/bin/python3
"""Module 0. Prime Game
This module contains an implementation
of a game played by Maria and Ben.
The game is based on prime numbers
and involves selecting numbers from a list
to determine the winner. Each
player strategically chooses numbers in a
specific sequence, aiming to
maximize their chances of winning.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game based on the rules provided.
    Parameters:
    x (int): The number of rounds to be played. Each
    round corresponds to an element in the list `nums`.
    nums (list): A list of integers, where each integer
    represents the maximum number in the current round.
    Returns:
    str: "Maria" if Maria wins more rounds, "Ben"
    if Ben wins more rounds, or None in case of a tie or invalid input.
    The function works by:
    1. Generating a sieve of primes up to the largest number in `nums`.
    2. Counting the number of primes for each round and
    determining the winner based on the rules.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0  # Tracks the number of rounds Ben wins
    maria = 0  # Tracks the number of rounds Maria wins

    # Generate a list to represent whether numbers are prime
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0  # 0 and 1 are not prime numbers

    # Use a sieve to mark multiples of primes as non-prime
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Count primes in the relevant range for each round and determine winner
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1  # Ben wins the round if the count of primes is even
        else:
            maria += 1  # Maria wins the round if the count of primes is odd

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Marks all multiples of a given number as non-prime in a sieve.
    Parameters:
    ls (list): A list representing primality,
    where 1 indicates a number is prime and 0 indicates it is not.
    x (int): The prime number whose multiples are to be marked as non-prime.
    The function iterates through the list and
    sets the values of all multiples of `x` to 0.
    It gracefully handles cases where indices go out of range.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0  # Mark multiple of `x` as non-prime
        except (ValueError, IndexError):
            break  # Stop if an index is out of bounds
