"""Eular problem 4 -
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

import timer
from toolkit import largest_palindrome

DESC = 'Largest palindrome product'
SOLUTION = 906609


@timer.timeit
def solve():
    return largest_palindrome(100, 1000)