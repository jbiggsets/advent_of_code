"""
Advent of Code, Day 2
date :: 12-02-2020
author :: Jeremy Biggs
"""

import argparse
import re


REGEX = re.compile(r'([0-9]{1,2})\-([0-9]{1,2})\s([a-z])\:\s([a-z].+)')


def _preprocess(filename):
    with open(filename) as fb:
        data = []
        for line in fb.readlines():
            nmin, nmax, letter, password = re.match(REGEX, line).groups()
            data.append((int(nmin), int(nmax), letter, password))
        return data


def count_policy_violations(line):
    """
    line : tuple of (int, int, char, str)
    """
    nmin, nmax, letter, password = line
    n = password.count(letter)
    return n >= nmin and n <= nmax


def count_new_policy_violations(line):
    """
    line : tuple of (int, int, char, str)
    """
    nmin, nmax, letter, password = line
    return ((password[nmin - 1] == letter) ^ (password[nmax - 1] == letter))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 2')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(sum(count_policy_violations(line) for line in data), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(sum(count_new_policy_violations(line) for line in data), '\n')
