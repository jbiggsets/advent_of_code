"""
Advent of Code, Day 8
date :: 12-08-2020
author :: Jeremy Biggs
"""

import argparse
from copy import deepcopy


def _preprocess(filename):
    with open(filename) as fb:
        return [i.split() for i in fb.read().strip().split('\n')]

class GameConsole:
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.idx = 1
        self.val = 0
        self.visited = []
    
    def jmp(self, inst):
        self.visited.append(self.idx)
        self.idx += int(inst)
        
    def acc(self, inst):
        self.visited.append(self.idx)
        self.val += int(inst)
        self.idx += 1
        
    def nop(self, inst):
        self.visited.append(self.idx)
        self.idx += 1
        
    def execute(self, stop_if_revisit=True):
        while True:
            # break if `stop_if_revist` set and the index was visisted
            if self.idx in self.visited and stop_if_revisit:
                break
            # break if the index is greater than the instruction set,
            # but add the index to the list of visited instructions
            if self.idx > len(self.instructions):
                self.visited.append(self.idx)
                break
            op, arg = self.instructions[self.idx - 1]
            getattr(self, op)(arg)
        return self


def fix_instructions_get_val(inst):

    # brute force search, changing each 'nop' and 'jmp' instruction
    for i in range(len(inst)):
        curr_inst = inst[i][0]
        if curr_inst in ('nop', 'jmp'):

            # get a temporary set, with the specific instruction changed
            inst_temp = deepcopy(inst)
            inst_temp[i][0] = 'nop' if curr_inst == 'jmp' else 'jmp'

            # run the console, with the instruction changed
            game = GameConsole(inst_temp).execute()
            if game.visited[-1] == len(inst_temp) + 1:
                return game.val

            del game
            del inst_temp


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 8')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    # problem 1
    print('Problem 1 Solution: ')
    print(GameConsole(data).execute().val, '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(fix_instructions_get_val(data), '\n')
