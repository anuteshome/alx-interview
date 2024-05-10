#!/usr/bin/python3
"""
This module contains a function called `island_perimeter` that
calculates the perimeter of the island in the given grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.

    Args:
        grid (list): A list of lists representing the grid.
                     0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.

    Raises:
        ValueError: If the grid is not rectangular or if its width or height
    exceeds 100.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Check if the grid is rectangular and within the size limits
    if any(len(row) != cols for row in grid):
        raise ValueError("The grid is not rectangular.")

    if rows > 100 or cols > 100:
        raise ValueError("The width or height of the grid exceeds 100.")

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell found
                # Check neighboring cells
                neighbors = 0
                if i - 1 < 0 or grid[i - 1][j] == 0:  # Up
                    neighbors += 1
                if i + 1 >= rows or grid[i + 1][j] == 0:  # Down
                    neighbors += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:  # Left
                    neighbors += 1
                if j + 1 >= cols or grid[i][j + 1] == 0:  # Right
                    neighbors += 1
                perimeter += neighbors

    return perimeter
