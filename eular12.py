"""
Eular 12: Triangle numbers
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be:
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred
divisors?
"""

import factors


# Generator
def triangle_num():
    x = 1
    tri = 1
    while True:
        yield tri
        x += 1
        tri += x


if __name__ == "__main__":
    for t in triangle_num():
        f = factors.divisors(t)

        if len(f) > 500:
            print('{} is the first triangle number to have over 500 divisors.'.format(t))

        print('{} has {} factors'.format(t, len(f)))
        #  print('{} has {} factors: {}'.format(t, len(f), f))

       #  if t > 100:
            #  exit()
