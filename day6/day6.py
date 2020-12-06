"""
Advent of Code, Day 6
date :: 12-06-2020
author :: Jeremy Biggs
"""

if __name__ == '__main__':

    with open('day6.txt') as fb:
        lines = fb.read()

    # get the groups
    groups = [group.split() for group in lines.strip().split('\n\n')]

    # get the group letters and the unique letter set
    groups_letters = [[letter for p in grp for letter in p] for grp in groups]
    unique_letters = set([letter for grp in groups_letters for letter in grp])

    # problem 1
    print('Problem 1 Solution: ')
    print(sum(len(set(grp)) for grp in groups_letters), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(sum([sum(all([(l in p) for p in grp]) for l in unique_letters)
               for grp in groups]), '\n')