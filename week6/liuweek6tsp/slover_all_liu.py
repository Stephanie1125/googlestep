#!/usr/bin/env python3
# for small number of N
# N = 16 not working

import math
import sys
from itertools import permutations


def read_input(filename):
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


def min_distance(cities):
    track_d = set()
    track_min = {}
    d = 0
    all_possible_perm = all_permutation(len(cities))
    for l in all_possible_perm:
        for i in range(1, len(l)):
            d += distance(cities[l[i-1]], cities[l[i]])
        d += distance(cities[l[-1]],cities[l[0]])
        track_d.add(d)
        track_min[d] = l
        d = 0
    min_d = min(track_d)
    return min_d, track_min[min_d]


def all_permutation(N):
    """
    for N=5 --> 5! = 120
    for N=8 --> 8!
    """
    index_list = [x for x in range(N)]
    return list(permutations(index_list))


if __name__ == '__main__':
    assert len(sys.argv) > 1
    xy_list = read_input(sys.argv[1])
    d = min_distance(xy_list)
    print("distance: %f" % d[0])
    print_format_solution(d[1])
