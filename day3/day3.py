"""
Advent of Code, Day 3
date :: 12-03-2020
author :: Jeremy Biggs
"""

import argparse
from math import prod


def _preprocess(filename):
    with open(filename) as fb:
        data = [line.strip() for line in fb.readlines() if line]
        return [[0 if cell == '.' else 1 for cell in row] * len(data)
                for row in data]


def find_trees_for_slope(grid, i=1, j=3):
    """
    Find the number of trees for a given slope.
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

    parser = argparse.ArgumentParser(description='Advent of Code, Day 3')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(find_trees_for_slope(data), '\n')

    # problem 2
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print('Problem 2 Solution: ')
    print(prod(find_trees_for_slope(data, i=i, j=j) for i, j in slopes), '\n')
