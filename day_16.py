'''
https://adventofcode.com/2020/day/16
'''
DAY = 16

from utils import *
import re


def parser(test=False):
    input_raw = Input(DAY, 2020, test=test)
    end_of_rules = input_raw.index('')

    # Parse the rules
    rules = {}
    for l, line in enumerate(input_raw[:end_of_rules]):
        match_rules = re.search(r"([\w+ ]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
        if match_rules:
            name, min1, max1, min2, max2 = match_rules.groups()
            rules[ name.replace(' ', '_') ] = (int(min1), int(max1), int(min2), int(max2))
        else:
            break

    # Parse my ticket
    if input_raw[end_of_rules+1] == 'your ticket:': # Check the line
        my_ticket = tuple(int(n) for n in input_raw[end_of_rules+2].split(','))
    else:
        raise IndexError

    # Parse nearby tickets
    if input_raw[end_of_rules+4] != 'nearby tickets:': # Check the line
        raise IndexError

    nearby_tickets = []
    for line in input_raw[end_of_rules+5:]:
        if not line:
            break
        nearby_tickets.append( tuple(int(n) for n in line.split(',')) )

    return rules, my_ticket, nearby_tickets


def check_rules(rules, ticket):
    checksum = 0
    for field in ticket:
        for min1, max1, min2, max2 in rules.values():
          if (min1 <= field <= max1) or (min2 <= field <= max2):
              break
        else: # nobreak -> rule was verified
            checksum += field
    
    return checksum


def part1(input):
    rules, _, nearby_tickets = input

    checksum = 0
    for ticket in nearby_tickets:
        checksum += check_rules(rules, ticket)

    return checksum


def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [71], part2, [])
    main()