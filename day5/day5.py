"""
Advent of Code, Day 5
date :: 12-05-2020
author :: Jeremy Biggs
"""

import argparse


def _preprocess(filename):
    with open(filename) as fb:
        return [l.strip() for l in fb.readlines() if l]


def find_seat_on_axis(seq, smax, lower_letter):
    rmin, rmax = 0, smax - 1
    for letter in seq:
        if letter == lower_letter:
            rmax -= (rmax - rmin) // 2 + 1
        else:
            rmin += (rmax - rmin) // 2 + 1
    return rmin

def find_seat_id(ticket, nrows=128, ncols=8):
    row = find_seat_on_axis(ticket[:7], nrows, 'F')
    col = find_seat_on_axis(ticket[7:], ncols, 'L')
    return row * 8 + col

def find_my_seat(seat_ids):
    for i in range(min(seat_ids) + 1, max(seat_ids) - 1):
        if i not in seat_ids and i + 1 in seat_ids and i - 1 in seat_ids:
            return i

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Advent of Code, Day 5')
    parser.add_argument('input_file', help='input file')
    args = parser.parse_args()

    data = _preprocess(args.input_file)

    seat_ids = [find_seat_id(ticket) for ticket in data]

    # problem 1
    print('Problem 1 Solution: ')
    print(max(seat_ids), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(find_my_seat(seat_ids), '\n')
