#!/usr/bin/env python3
# coding=utf-8

"""
Eular15

*Lattice paths*

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


#  while path[0] == (0, 0):


def next_path(path, grid_len):
    while len(path) > 0:
        x, y = path.pop()  # Pop back one step
        if len(path) == 0:
            return False, []
        _x, _y = path[-1]

        if _x == grid_len or _y == grid_len:  # Wall. Only 1 choice available.
            pass
        elif y == _y + 1:
            pass
        else:
            path.append((_x, _y + 1))
            return True, path
    else:
        return False, []


def get_routes(x, y, grid_size, remembered={}):
    # Finds all the routes from a given point (x, y) in a grid.
    routes, path = [], []
    iterating = True

    while iterating:
        path.append((x, y))
        if x < grid_size:
            x += 1
        elif y < grid_size:
            y += 1
        else:
            routes.append(path[:])  # We have reached the end node
            iterating, path = next_path(path, grid_size)
            if iterating:
                x, y = path.pop()

        if (x, y) in remembered:
            for route in remembered[(x, y)]:
                newpath = path[:]
                newpath.extend(route)
                routes.append(newpath)
            path.append((x, y))

            iterating, path = next_path(path, grid_size)
            if iterating:
                x, y = path.pop()

    return routes


def find_all_routes(grid_size, remembered):
    # The lattice array is really grid_size + 1
    routes = get_routes(0, 0, grid_size, remembered)

    for i in range(grid_size, -1, -1):
        for j in range(grid_size, -1, -1):
            #  print('remembering the paths for ({}, {})...'.format(i, j))
            if (i, j) not in remembered:
                remembered[i, j] = get_routes(i, j, grid_size, remembered)

    routes = get_routes(0, 0, grid_size, remembered)

    count = 0
    """
    while len(routes) > 0:
        r = routes.pop()
        if r in routes:
            pass
        if len(r) == (grid_size * 2) + 1:
            count += 1
    """

    #  for r in routes:
        #  if len(r) == (grid_size * 2) + 1:
            #  count += 1

    #  return count
    return len(routes)


if __name__ == "__main__":
    for i in range(1, 12):
        remembered = {}
        print('{} routes in a {}x{} grid!'.format(find_all_routes(i, remembered), i, i))
