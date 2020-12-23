'''
https://adventofcode.com/2020/day/23
'''
DAY = 23

from utils import *
from collections import deque
from time import time


MOVES = 100
INPUTS = [
    '792845136', # My input
    '389125467', # Test 1
]


def parser(test=False):
    if not test:
        return INPUTS[0]
    else:
        return INPUTS[test]


def part1(input):
    cups = deque([int(i) for i in input])

    for t in range(MOVES):
        # Find current cup
        current = cups[0]

        # Rotate to be right to the group to be picked
        cups.rotate(-1)
        
        # Pick the group of three
        picked = [cups.popleft() for _ in range(3)]
        
        # Find the destination point
        destination = (current - 2)%9 + 1
        while destination in picked:
            destination = (destination - 2) %9 +1

        # Rotate to the destination point (to extend on the left)
        cups.rotate( -cups.index(destination)-1 )

        # Insert the picked cups
        cups.extend(picked)

        # Rotate to have the next current cup on [0]
        cups.rotate( -cups.index(current)-1 )

    # Rotate to have the 1 on the right
    cups.rotate( -cups.index(1)-1 )

    return ''.join([str(cups.popleft()) for _ in range(8)])


def part2(input):
    '''According to my calculations in a core i7 10th gen. it should take ~36h. '''
    cups = deque([int(i) for i in input])
    for i in range(1_000_000 - 9):
        cups.append(10+i)

    for t in range(10_000_000):
        # Find current cup
        current = cups[0]

        # Rotate to be right to the group to be picked
        cups.rotate(-1)
        
        # Pick the group of three
        picked = [cups.popleft() for _ in range(3)]
        
        # Find the destination point
        destination = (current - 2)%1_000_000 + 1
        while destination in picked:
            destination = (destination - 2) %1_000_000 +1

        # Rotate to the destination point (to extend on the left)
        cups.rotate( -cups.index(destination)-1 )

        # Insert the picked cups
        cups.extend(picked)

        # Rotate to have the next current cup on [0]
        cups.rotate( -cups.index(current)-1 )

    # Rotate to have the 1 on the right
    cups.rotate( -cups.index(1)-1 )

    return cups[0]*cups[1]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, ['67384529'], part2, []) 
    main()