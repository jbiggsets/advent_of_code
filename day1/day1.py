"""
Advent of Code, Day 1
date :: 12-01-2020
author :: Jeremy Biggs
"""

from itertools import combinations
from math import prod


def find_r_summing_to_x_and_take_product(arr, r=2, x=2020):
    """
    arr : list of int
        The list of numbers
    r : int, default=2
        How many numbers to pick (without replacement)
    x : int, default=2020
        The `x` that numbers in `arr` should sum to.
    """
    comb = combinations(arr, r)
    for c in comb:
        if sum(c) == x:
            return prod(c)


if __name__ == '__main__':

    with open('day1.txt') as fb:
        lines = [int(l.strip()) for l in fb.readlines()]

    # problem 1
    print('Problem 1 Solution: ')
    print(find_r_summing_to_x_and_take_product(lines), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(find_r_summing_to_x_and_take_product(lines, r=3), '\n')
