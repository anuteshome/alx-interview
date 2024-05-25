#!/usr/bin/python3

"""
This module contains four function which will help us to
determine the winner of the game. Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and
including n, they take turns choosing a prime number from the set and
removing that number and its multiples from the set. The player that
cannot make a move loses the game.
"""


def find_prime_num(numbers):
    """
    Finds the smallest prime number of a given list.

    Args:
            numbers (list): An array of integers.

    Returns:
            The smallest prime number or -1 if no prime number exist
            on the list.
    """
    for num in numbers:
        if num != 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            return num
    return -1


def find_multiple_of_num(number, numbers):
    """
    Finds a multiples of a given number.

    Args:
            number (int): Integer number

    Returns:
            List (list): list of multiples of given number.
    """
    multiples = []
    for i in numbers:
        if i % number == 0:
            multiples.append(i)
    return multiples


def check_move(numbers):
    """
    Checks if the player can make a move.

    Args:
        numbers (list): An array of integers

    Returns:
        List (list): If they can make a move else None. If prime
        number is not in the list it means no movement.
    """
    choice = find_prime_num(numbers)
    if choice == -1:
        return None
    elements_to_remove = find_multiple_of_num(choice, numbers)
    numbers = [x for x in numbers if x not in elements_to_remove]
    return numbers


def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.

    Args:
            x (int): The number of rounds of the game.
            nums (list): An array of integer.

    Returns:
            The name of the player that won the most rounds.
            If the winner cannot be determined it returns None.
    """
    if not nums or x < 1:
        return None

    maria_win = 0
    ben_win = 0
    for round in nums:
        numbers = list(range(1, round + 1))
        maria_turn = True
        while True:
            if maria_turn:
                moves = check_move(numbers)
                if moves is None:
                    ben_win += 1
                    break
                numbers = moves
            else:
                moves = check_move(numbers)
                if moves is None:
                    maria_win += 1
                    break
                numbers = moves
            maria_turn = not maria_turn

    if maria_win > ben_win:
        return "Maria"
    elif maria_win < ben_win:
        return "Ben"
    return None
