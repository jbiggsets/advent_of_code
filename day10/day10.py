"""
Advent of Code, Day 10
date :: 12-10-2020
author :: Jeremy Biggs
"""

import argparse
from collections import Counter, defaultdict


def _preprocess(filename):
    with open(filename) as fb:
        return [int(d) for d in fb.read().strip().split('\n')]


def count_jolt_differences(data):
    current = 0
    counter = Counter()
    for adapter in sorted(data):
        counter.update([adapter - current])
        current = adapter
    counter.update([max(data) + 3 - current])
    return counter[1] * counter[3]


def count_jolt_arrangements(data, n=3):
    data = sorted(data) + [max(data) + n]
    paths = defaultdict(lambda: 0)
    paths[0] += 1
    for adapter in data:
        for previous_i in range(1, n + 1):
            previous_adapter = adapter - previous_i
            if previous_adapter in paths:
                paths[adapter] += paths[previous_adapter]
    return paths[data[-1]]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 10')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(count_jolt_differences(data), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(count_jolt_arrangements(data), '\n')
