#!/usr/bin/python3
"""
This module provides functions to solve the N Queens problem. The N Queens
problem is the problem of placing N chess queens on an N x N chessboard so
that no two queens threaten each other. In other words, no two queens can
share the same row, column, or diagonal.
"""
import sys


def is_safe(board, row, col):
    """
    Check if the current position is safe for a queen.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index of the current position.
        col (int): The column index of the current position.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check for queens in the diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def backtrack(row, N, board, solutions):
    """
    Recursive function to solve the N Queens problem using backtracking.

    Args:
        row (int): The current row being processed.
        N (int): The size of the chessboard (N x N).
        board (list): The current state of the chessboard.
        solutions (list): List to store the valid solutions.

    Returns:
        None
    """
    if row == N:
        # All queens have been placed, add the solution to the list
        solutions.append(board.copy())
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            backtrack(row + 1, N, board, solutions)


def solve_nqueens(N):
    """
    Function to solve the N Queens problem and print the solutions.

    Args:
        N (int): The size of the chessboard (N x N).

    Returns:
        None
    """
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board
    board = [-1] * N

    # Solve the N Queens problem
    solutions = []
    backtrack(0, N, board, solutions)

    # Print the solutions in the desired format
    for solution in solutions:
        print([[r, c] for r, c in enumerate(solution)])


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
