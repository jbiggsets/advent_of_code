"""
Advent of Code, Day 1
date :: 12-01-2020
author :: Jeremy Biggs
"""

import argparse
from itertools import combinations
from math import prod

def _preprocess(filename):
    with open(filename) as fb:
        return [int(l.strip()) for l in fb.readlines()]


def find_r_summing_to_x_and_take_product(arr, r=2, x=2020):
    """
    Find a combination of ``r`` numbers in the array, summing to ``x``
    """
    comb = combinations(arr, r)
    for c in comb:
        if sum(c) == x:
            return prod(c)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day1')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(find_r_summing_to_x_and_take_product(data), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(find_r_summing_to_x_and_take_product(data, r=3), '\n')
