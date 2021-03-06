"""
Advent of Code, Day 7
date :: 12-07-2020
author :: Jeremy Biggs
"""

import argparse
import re

REGEX = '([0-9]+)\s(.*)'


def _preprocess(filename):
    with open(filename) as fb:
        bags = fb.readlines()

    bags = [b.strip()\
             .replace('.', '')\
             .replace('bags', 'bag')\
             .split(' contain ') for b in bags]
    bags = {k: v.split(', ') for k, v in bags}
    bags = {k: {re.search(REGEX, v_i)[2]: int(re.search(REGEX, v_i)[1])
                for v_i in v if v_i.strip() != 'no other bag'}
            for k, v in bags.items()}
    return bags

    
class BagSearcher:

    def __init__(self, bags):
        self.bags = bags
        self.parents = set()
    
    def search(self, target):
        for key, value in self.bags.items():
            if target in value and key not in self.parents:
                self.parents.add(key)
                self.search(key)
        return self.parents


class BagCounter:

    def __init__(self, bags):
        self.bags = bags

    def _count(self, root):
        total = 1
        for bag, number in self.bags[root].items():
            total += number * self._count(bag)
        return total

    def count(self, root, include_root=False):
        if include_root:
            return self._count(root)
        # subtract the root bag itself
        return self._count(root) - 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 7')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(len(BagSearcher(data).search('shiny gold bag')), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(BagCounter(data).count('shiny gold bag'), '\n')
