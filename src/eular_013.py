"""Eular Problem 13 -
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.
"""

from src import timer

DESC = 'Large Sum'
SOLUTION = 5537376230


@timer.timeit
def solve():
    n = read_numbers('data/bignumbers.txt')
    bigsum = 0
    for x in n:
        bigsum += x

    sum_list = list(str(bigsum))
    return int(''.join(sum_list[0:10]))


def read_numbers(filename):
    """ Read each number as a line from the file and return the numbers as a list. """
    with open(filename) as f:
        numbers = [int(l) for l in f.readlines()]
    return numbers
