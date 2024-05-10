#!/usr/bin/python3
"""
Module: 0-minoperations

This module provides a function to calculate the minimum number of operations
required to reach a desired count of characters using the prime factorization
approach
"""
import math


def minOperations(n):
    """
    Calculates the minimum number of operations required to reach the desired
    count of 'H' characters using the prime factorization approach.

    Args:
    - n (int): The desired count of 'H' characters.

    Returns:
    - operations (int): The minimum number of operations required to reach
    the desired count.

    Example:
    >>> minOperations(100)
    12
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Check if n is prime
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        return n

    while factor <= math.isqrt(n):
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1
    if n > 1:
        operations += n

    return operations
