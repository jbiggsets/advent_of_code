"""
Advent of Code, Day 4
date :: 12-04-2020
author :: Jeremy Biggs
"""

import re


class Passport:
    
    _expected = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    _hair_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    
    def __init__(self, fields_dict):
        self.fields = fields_dict

    @staticmethod
    def val_regex(field, regex):
        match = re.match(regex, field)
        return match and match.group() == field

    @staticmethod
    def val_date(field, start, end, dig=4):
        return len(str(field)) == dig and int(field) >= start and int(field) <= end

    @staticmethod    
    def val_height(field):
        match = re.match('([0-9]{1,3})(cm|in)', field)
        if match:
            val, msr = match.group(1), match.group(2)
            if ((msr == 'cm' and int(val) >= 150 and int(val) <= 193) or
                (msr == 'in' and int(val) >= 59 and int(val) <= 76)):
                return True            
        return False

    def validate(self, include_values=False):
        check_fields = all(f in self.fields for f in self._expected)
        if check_fields and include_values:
            return all([self.val_date(self.fields['byr'], 1920, 2002),
                        self.val_date(self.fields['iyr'], 2010, 2020),
                        self.val_date(self.fields['eyr'], 2020, 2030),
                        self.val_regex(self.fields['hcl'], '#[0-9a-f]{6}'),
                        self.val_regex(self.fields['pid'], '[0-9]{9}'),
                        self.val_height(self.fields['hgt']),
                        self.fields['ecl'] in self._hair_colors])
        return check_fields


if __name__ == '__main__':

    with open('day4.txt') as fb:
        passports = [{i.split(':')[0]: i.split(':')[-1]
                      for i in re.sub('\s', ' ', l).split(' ')}
                     for l in fb.read().split('\n\n')]

    # problem 1
    print('Problem 1 Solution: ')
    print(sum(Passport(p).validate() for p in passports), '\n')

    # problem 2
    print('Problem 2 Solution: ')
    print(sum(Passport(p).validate(True) for p in passports), '\n')
