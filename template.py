'''
https://adventofcode.com/2020/day/
'''
DAY = 0

from utils import *


def part1(input):
    pass


def part2(input):
    pass


def test():
    # Test number:
    tests_results = []

    print('Part 1:')
    for test_i, test_result in enumerate(tests_results, 1):
        input = Input(DAY, 2019, test=test_i)
        result = part1(input)
        assert result == test_result
        print(f'Test {test_i} CORRECT')
    
    print('-----------------------------------------')
    print(' ')
    print('Part 2:')

    # Test number:   
    tests_results_2 = []

    for test_i, test_result in enumerate(tests_results_2, 1):
        input = Input(DAY, 2019, test=test_i)
        result = part2(input)
        assert result == test_result
        print(f'Test {test_i} CORRECT')
    

def main():
    tests()
    
    input = Input(DAY, 2020)
    part1(input)
    # part2(input)


if __name__ == "__main__":
    main()