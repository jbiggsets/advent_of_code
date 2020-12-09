"""
Advent of Code, Day 9
date :: 12-09-2020
author :: Jeremy Biggs
"""

import argparse
from itertools import combinations


def _preprocess(filename):
    with open(filename) as fb:
        return [int(n) for n in fb.read().strip().split('\n')]


def decrypter(data, preamble=25):
    for i, n in enumerate(data[preamble:]):
        numbers = data[i: preamble + i]
        candidates = set([sum(c) for c in combinations(numbers, 2)])
        if n not in candidates:
            return n

def contiguous_number_finder(data, target):
    for i in range(len(data)):
        j, count = i, 0
        while count <= target:
            count += data[j]
            if count == target:
                return min(data[i:j + 1]) + max(data[i:j + 1])
            j += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 9')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(decrypter(data), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(contiguous_number_finder(data, decrypter(data)), '\n')
