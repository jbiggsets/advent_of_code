"""
Advent of Code, Day 2
date :: 12-02-2020
author :: Jeremy Biggs
"""

import re


REGEX = re.compile(r'([0-9]{1,2})\-([0-9]{1,2})\s([a-z])\:\s([a-z].+)')


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

    with open('day2.txt') as fb:
        lines = []
        for line in fb.readlines():
            nmin, nmax, letter, password = re.match(REGEX, line).groups()
            lines.append((int(nmin), int(nmax), letter, password))

    # problem 1
    print('Problem 1 Solution: ')
    print(sum(count_policy_violations(line) for line in lines), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(sum(count_new_policy_violations(line) for line in lines), '\n')
