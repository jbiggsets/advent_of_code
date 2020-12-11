"""
Advent of Code, Day 11
date :: 12-11-2020
author :: Jeremy Biggs
"""

from copy import deepcopy
from itertools import product


def _preprocess(filename):
    with open(filename) as fb:
        return [[i for i in l.strip()] for l in fb.readlines()]


class SeatingSystem:
    
    _directions = list(product([-1, 0, 1], repeat=2))
    _directions.remove((0, 0))
    
    def __init__(self, seats,
                 use_nearest=True,
                 min_occupied=4,
                 max_iter=200):
        self.seats = deepcopy(seats)
        self.prev = []
        self.n = len(seats)
        self.m = len(seats[0])

        self.min_occ = min_occupied
        self.max_iter = max_iter
        
        self.func = (self.find_neighbors
                     if use_nearest
                     else self.find_firsts)

    def apply_rules(self, seat, neighbors):
        if seat == 'L' and '#' not in neighbors:
            return '#'
        elif (seat == '#' and 
              sum(n == '#' for n in neighbors) >= self.min_occ):
            return 'L'
        return seat

    def find_neighbors(self, i, j, seats, dist=1):
        i_min, i_max = max(0, i - dist), min(i + dist + 1, self.n)
        j_min, j_max = max(0, j - dist), min(j + dist + 1, self.m)
        neighbors = []
        for row in range(i_min, i_max):
            for col in range(j_min, j_max):
                if (row, col) != (i, j):
                    neighbors.append(seats[row][col])
        return neighbors

    def find_firsts(self, i, j, seats):
        firsts = []
        for i_dir, j_dir in self._directions:
            i_cur, j_cur = i + i_dir, j + j_dir
            while (i_cur < self.n and i_cur >= 0 and
                   j_cur < self.m and j_cur >= 0):
                if seats[i_cur][j_cur] in ['#', 'L']:
                    firsts.append(seats[i_cur][j_cur])
                    break
                i_cur += i_dir; j_cur += j_dir
        return firsts

    def rearrange(self):
        self.prev.append(deepcopy(self.seats))
        for i in range(self.n):
            for j in range(self.m):
                neighbors = self.func(i, j, self.prev[-1])
                self.seats[i][j] = self.apply_rules(self.prev[-1][i][j],
                                                    neighbors)
                del neighbors
        return self

    def solve(self):
        i = 0
        while self.seats not in self.prev:
            self.rearrange(); i += 1
            if i == self.max_iter:
                break
        return self


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 11')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    s1 = SeatingSystem(data, True, 4).solve()
    print(sum(seat == '#' for row in s1.seats for seat in row), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    s2 = SeatingSystem(data, False, 5).solve()
    print(sum(seat == '#' for row in s2.seats for seat in row), '\n')
