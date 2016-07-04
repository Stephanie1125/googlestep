import sys
import math
import doctest


def read_input(filename):
    """
    >>> r = read_input('test.csv')
    >>> print r
    [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
    """
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def print_format_solution(solution):
    print ('index\n' + '\n'.join(map(str, solution)))


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    pass


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_format_solution(solution)


doctest.testmod(verbose=1)