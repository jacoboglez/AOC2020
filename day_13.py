'''
https://adventofcode.com/2020/day/13
'''
DAY = 13

from utils import *


def parser(test=False):
    earliest, buses = Input(DAY, 2020, test=test)
    return (int(earliest), [b if b=='x' else int(b) for b in buses.split(',')])


def part1(input):
    my_time, buses = input

    earliest_bus = float('inf')
    min_wait = float('inf')
    for bus in buses:
        if bus == 'x':
            continue

        wait_time = bus - (my_time % bus)
        if wait_time < min_wait:
            min_wait = wait_time
            earliest_bus = bus

    # print(f'{earliest_bus=}')
    # print(f'{wait_time=}')
    return earliest_bus * min_wait


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
    try:
        test(DAY, parser, part1, [295], part2, [])
    except AssertionError:
        pass
    main()