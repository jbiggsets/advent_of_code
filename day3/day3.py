"""
Advent of Code, Day 3
date :: 12-03-2020
author :: Jeremy Biggs
"""

from math import prod


def find_trees_for_slope(grid, i=1, j=3):
    """
    Find the number of trees for a given slope.

    grid : list of list of int
        The skiiing course grid
    i : int
        The i of the slope
    j : int
        The j of the slope
    """
    n_rows = len(grid) - 1
    i_row, j_col, trees = 0, 0, 0
    while i_row <= n_rows:

        is_tree = int(grid[i_row][j_col] == 1)
        trees += is_tree

        i_row += i
        j_col += j

    return trees


if __name__ == '__main__':

    with open('day3.txt') as fb:
        data = [line.strip() for line in fb.readlines() if line]
        grid = [[0 if cell == '.' else 1 for cell in row] * len(data)
                for row in data]

    # problem 1
    print('Problem 1 Solution: ')
    print(find_trees_for_slope(grid), '\n')

    # problem 2
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print('Problem 2 Solution: ')
    print(prod(find_trees_for_slope(grid, i=i, j=j) for i, j in slopes), '\n')
