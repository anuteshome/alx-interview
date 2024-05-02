#!/usr/bin/python3
"""
This module contains a function called `makeChange` that calculates
the minimum number of coins needed to make a specific total using
a given set of coin denominations.
"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make a specific
    total using a given set of coin denominations.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target total to be achieved.

    Returns:
        int: The minimum number of coins needed to make the total.
        If it's not possible to make the exact total with the given
        coins, returns -1.

    Raises:
        None

    Example:
        >>> coins = [1, 5, 10, 25]
        >>> total = 30
        >>> makeChange(coins, total)
        2
    """

    # Check if the total is non-positive
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    # Initialize a variable to count the number of coins used
    count = 0

    for coin in coins:
        if total >= coin:
            # Calculate the number of coins of the current denomination
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin

    # If the total amount is not zero, it cannot be met by any number of coins
    if total != 0:
        return -1

    return count
