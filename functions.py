import itertools
import math
import primes


def abundant(n):
    """
    A number n is called abundant if the sum of its proper divisors is more than n. Returns True
    if n is an abundant number, False otherwise.
    """
    return sum(divisors_proper(n)) > n


def abundants_upto(limit):
    """
    Returns a list of all abundant numbers up, and including, the limit.
    """
    return [i for i in range(1, limit + 1) if abundant(i)]


def add_amicables(limit):
    """
    Adds all the amicable numbers up to limit and returns the sum.
    """
    amicables = set()
    div_sums = divisor_sum_dict(limit)

    for k, v in div_sums.items():
        # Skip divisor sums that are equal to or over the limit - they won't be in the keys.
        # Also - k and v cannot be equal. k != v.
        if v >= limit or k == v:
            continue

        # Since we have the divisor sum of k as v, we can conversely lookup the opposite
        # div_sums[v] and check if it equals k.
        if div_sums.get(v, -1) == k:
            amicables.add(k)

    return sum(amicables)


def alphabetical_value(name):
    """
    Returns the sum of the alphabetical values of the string passed. Each letter is equal to it's
    position in the alphabet.
    Example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53
    """
    return sum([ord(x.lower()) - 96 for x in list(name)])


def collatz_seq(n, collatz_dict={}):
    """
    Takes an integer n and returs the resulting Collatz sequence as a list.
    """
    seq = [n]
    while n > 1:
        n = next_collatz(n)
        if n in collatz_dict:
            seq.extend(collatz_dict[n])
            collatz_dict[seq[0]] = seq
            return seq
        else:
            seq.append(n)

    collatz_dict[seq[0]] = seq
    print(seq)
    return seq


def div_by_all_upto(limit):
    """
    Finds the first integer that is divisible by all numbers 1 through, and including, limit.
    """
    # Start at the highest factor we are testing by because the target number won't be divisible
    # by any numbers larger than it.
    if limit < 10:
        raise ValueError('This function only tests for ranges 10 and above!')
    elif limit % 10 != 0:
        raise ValueError('This function only tests multiples of 10!')

    i = limit

    while True:
        # Skip any number that doesn't end in 0.
        # Ending in 0 maximizes our chance of a big divisor.
        if i % 10 != 0:
            pass
        elif factor_of_all_upto(i, limit):
            break

        # Increase by the size of the largest factor we are testing by. This should dramatically
        # increase the speed and we don't need to test numbers in between since they won't be
        # divisible by that number.
        i += limit
    return i


def divisors_bruteforce(n):
    """
    Returns a set of all the divisors of n using a brute force check.  We only need to check up
    to (n/2) for any n, because n won't be divisible by anything larger than that. We'll also
    skip checking even divisors for odd numbers, since they won't be divisible, however this is
    still pretty slow for numbers over a million.
    """
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')

    factors = set()
    middle = n // 2

    if n % 2 == 0:  # It's even
        for i in range(1, middle + 1):
            if n % i == 0:
                factors.add(i)
    else:
        # It's odd (skip checking even factors)
        for i in range(1, middle + 1, 2):
            if n % i == 0:
                factors.add(i)

    # n will ALWAYS be a factor of itself.
    factors.add(n)
    return factors


def divisors(n):
    """
    Creates a list of all the factors of n and returns them as a set. First we get the prime
    factors of n. To get any remaining factors, we take all the prime factors and take each to
    it's maximum power. This results in a list of factors we can use to build the remaining
    factors.
    """
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')
    elif n == 1:
        return {1}

    prime_facts = primes.get_prime_factors(n)
    if prime_facts is None:
        return None

    factors = list(prime_facts)

    for x in factors:
        for y in factors:
            product = y * x

            if n % product == 0 and product not in factors:
                factors.append(product)

    # Cutting out 1 saves a lot of checks and is a factor of every positive number.
    factors.append(1)
    return set(factors)


def divisors_proper(n):
    """
    Return a set containing the proper divisors of n (numbers less than n which divide evenly
    into n).
    """
    d = divisors(n)
    d.remove(n)
    return d


def divisor_sum_dict(limit):
    """
    Make a dictionary of divisor sums up to, but not including, limit.
    Example: The divisor sum of 2 would be 1 + 2 = 3.
             The divisor sum of 220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
    """
    return {n: sum_proper_divisors(n) for n in range(1, limit)}


def factor_of_all_upto(num, limit):
    """
    Returns True if num is divisible by all numbers in the range of integers in 1 up to and
    including limit.
    # Speed up by skipping 1. Any integer is divisible by 1!
    # If the number ends in 1, 3, 7, or 9, it's more likely to be prime.
    # Check backwards from the largest possible factor
    """
    start = 2
    for factor in range(start, limit + 1):
        if num % factor != 0:
            return False
    return True


def factorial_sum(n):
    """
    Returns the sum of the integers in the factorial of n.
    """
    return sum([int(x) for x in str(math.factorial(n))])


def fibonaccis(limit=None):
    """
    Defines a Fibonacci number generator. The sequence returned is [1, 1, 2, 3, 5] and so on
    as the sequence progresses.
    """
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            raise StopIteration()
        a, b = b, a + b
        yield a


def is_palindrome(number):
    """
    Returns True if the variable passed is a palindrome, False otherwise.
    """
    numlist = list(str(number))

    if len(numlist) <= 0:
        return False
    if len(numlist) == 1:
        return True

    i = 0
    while i <= len(numlist) / 2:
        if numlist[i] != numlist[-(i+1)]:
            return False
        i += 1
    else:
        return True


def largest_palindrome(lowerlimit, upperlimit):
    """
    Finds the largest palindrome in the given integer limits.
    """
    largest_palindrome = 0

    for m1 in range(lowerlimit, upperlimit):
        # Start from m1 for this range so we don't hit duplicate factors
        for m2 in range(m1, upperlimit):
            product = m1 * m2
            if is_palindrome(product):
                # print("Found palindrome!: {}".format(product))
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome


def longest_collatz_seq(upto):
    """
    Finds the longest collatz sequence in all the integers 0 to the upto integer passed and
    returns is as a list.
    """
    collatz_dict = {}
    longestseq = []
    for i in range(1, upto):
        seq = collatz_seq(i, collatz_dict)
        if len(seq) > len(longestseq):
            longestseq = seq
    return seq


def next_collatz(n):
    """
    Takes an integer n and returns the following integer in the Collatz sequence.

    If n is even, it returns n divided by 2.
    If n is odd, it returns (3*n) + 1.

    The end of a collatz sequence is traditionally 1, so we will raise an exception if the n
    passed is 1.
    """
    if n <= 1:
        raise ValueError('eular14.next_collatz: n must be a positive integer larger than 1!')
    elif n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def nonsummable_by_abundants():
    LIMIT = 28123
    # Calculate all the abundant numbers up to limit.
    abundants = abundants_upto(LIMIT)

    # Create all possible 2 term combinations for sums.
    #  pairs = list(itertools.combinations(abundants, 2)) # No
    #  pairs = itertools.combinations(abundants, 2) # No
    #  pairs = itertools.permutations(abundants, 2) # No
    # We want the Cartesian product, because the abundant numbers, can be repeated(ex: 12 - the
    # lowest abundant number, can be repeated 12+12 to sum 24.)
    pairs = itertools.product(abundants, repeat=2)

    # Create a set of sums using a set comprehension
    abundant_sums = {a + b for a, b in pairs}

    unsummable = [i for i in range(LIMIT + 1) if i not in abundant_sums]

    # Return the sum of all integers that cannot be written as the sum of abundant numbers.
    return sum(unsummable)


def sum_of_squares(limit):
    """
    Returns the sum of all squares in the range 1 up to and including limit.
    """
    return sum([i ** 2 for i in range(limit+1)])


def sum_proper_divisors(n):
    """
    Return the sum of the proper divisors of n(numbers less than n which divide evenly into n).
    """
    divisors = divisors_proper(n)
    return sum(divisors)


def square_of_sum(limit):
    """
    Returns the square of the sum of all integers in the range 1 up to and including limit.
    """
    return sum([i for i in range(limit + 1)]) ** 2


def triangles():
    """
    Defines a generator that generates triangle numbers. The sequence of triangle numbers is
    generated by adding the natural numbers. The first triangle number is 1, followed by 3, 6,
    10, and so on.
    """
    x = 1
    tri = 1
    while True:
        yield tri
        x += 1
        tri += x
