#!/usr/bin/python3

"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list): The 2D matrix to be rotated.
        Assumed to be a square matrix.

    Returns:
        None: The matrix is edited in place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        rotate_2d_matrix(matrix)

        # Print the rotated matrix
        for row in matrix:
            print(row)

        Output:
        [7, 4, 1]
        [8, 5, 2]
        [9, 6, 3]
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
