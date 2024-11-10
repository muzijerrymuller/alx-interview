#!/usr/bin/python3
"""
N-Queens Solution Finder
This program provides a solution to the classic
N-Queens problem, a challenge in
which N queens must be placed on an N x N
chessboard in such a way that none of
the queens are able to attack each other.
This implementation leverages a
backtracking algorithm to explore and
identify all unique arrangements for the
queens that satisfy the non-attacking requirement.
Usage:
    python3 nqueens.py N
Where N is an integer greater than or equal to 4.
"""

import sys


def place_queens(
        row,
        board_size,
        column_set,
        positive_diagonal_set,
        negative_diagonal_set,
        board_state
    ):
    """
    Recursive backtracking function to place queens on the chessboard.
    This function attempts to place a queen in each row of the chessboard.
    If a queen placement in a specific column or diagonal conflicts with
    another queen, the function backtracks and attempts an alternative path.
    Args:
        row (int): The current row to attempt to place a queen.
        board_size (int): The size of the chessboard (N x N).
        column_set (set): Columns that already contain a queen.
        positive_diagonal_set (set): Positive diagonals
        that already contain a queen.
        negative_diagonal_set (set): Negative
        diagonals that already contain a queen.
        board_state (list of lists): The N x N
        board representing queen placements.
    """
    if row == board_size:
        solution = []
        for r in range(board_size):
            for c in range(board_size):
                if board_state[r][c] == 1:
                    solution.append([r, c])
        print(solution)
        return

    for column in range(board_size):
        if column in column_set or (row + column) in positive_diagonal_set
        or (row - column) in negative_diagonal_set:
            continue

        column_set.add(column)
        positive_diagonal_set.add(row + column)
        negative_diagonal_set.add(row - column)
        board_state[row][column] = 1

        place_queens(
                row + 1,
                board_size,
                column_set,
                positive_diagonal_set,
                negative_diagonal_set,
                board_state
            )

        column_set.remove(column)
        positive_diagonal_set.remove(row + column)
        negative_diagonal_set.remove(row - column)
        board_state[row][column] = 0


def solve_nqueens(board_size):
    """
    Initialize and solve the N-Queens problem for a specified board size.
    This function sets up the necessary data structures and calls the
    recursive backtracking function to determine all solutions to the N-Queens
    problem for the given board size. It ensures that solutions are generated
    without duplicate placements where queens threaten each other.
    Args:
        board_size (int): The number of queens and the
        size of the chessboard (N).
    """
    column_set = set()
    positive_diagonal_set = set()
    negative_diagonal_set = set()
    board_state = [[0] * board_size for _ in range(board_size)]

    place_queens(
            0,
            board_size,
            column_set,
            positive_diagonal_set,
            negative_diagonal_set,
            board_state
            )


if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(arguments[1])
        if board_size < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(board_size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
