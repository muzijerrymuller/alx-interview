#!/usr/bin/python3
"""
Island Perimeter Problem
========================
This module provides a function to calculate the perimeter of an island
described in a 2D grid. Each cell in the grid can either represent water (0)
or land (1). The function adheres to specific rules of connectivity and grid
structure to compute the exact perimeter of the landmass.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    The island is represented as a group of connected land cells (1s) within
    a 2D grid, surrounded by water (0s). The function computes the perimeter
    based on the following rules:
    - Each land cell contributes 4 to the perimeter initially.
    - For each adjacent land cell, the shared edge reduces the perimeter by 1.
    Constraints:
    - The grid is rectangular, with a width and height not exceeding 100.
    - There is exactly one island or no island at all.
    - The island has no internal lakes (water surrounded entirely by land).
    Args:
        grid (list[list[int]]): A 2D list of integers where:
            - 0 represents water.
            - 1 represents land.
    Returns:
        int: The total perimeter of the island.
    Example:
        >>> grid = [
        ...     [0, 1, 0, 0],
        ...     [1, 1, 1, 0],
        ...     [0, 1, 0, 0],
        ...     [1, 1, 0, 0]
        ... ]
        >>> island_perimeter(grid)
        16
    """
    # Initialize perimeter to zero
    perimeter = 0

    # Iterate through each cell in the grid
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] == 1:
                if row_index == 0 or grid[row_index - 1][col_index] == 0:
                    perimeter += 1
                if row_index == len(grid) - 1 or grid[row_index + 1][col_index] == 0:
                    perimeter += 1
                if col_index == 0 or grid[row_index][col_index - 1] == 0:
                    perimeter += 1
                if col_index == len(grid[row_index]) - 1 or grid[row_index][col_index + 1] == 0:
                    perimeter += 1

    return perimeter
