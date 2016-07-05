"""
Python3
for small number of N
N=5 --> 5! = 120
N=8 --> 8!
N=16 --> not working
"""

import math
import sys
from itertools import permutations
from functions import *


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def min_distance(cities):
    track_min = {}
    all_possible_perm = all_permutation(len(cities))
    for path in all_possible_perm:
        d = 0
        for i in range(1, len(path)):
            d += distance(cities[path[i-1]], cities[path[i]])
        d += distance(cities[path[-1]], cities[path[0]])
        track_min[d] = path
    min_d = min(track_min)
    return min_d, track_min[min_d]


def all_permutation(n):
    index_list = [x for x in range(n)]
    return list(permutations(index_list))


if __name__ == '__main__':
    assert len(sys.argv) > 1
    xy_list = read_input(sys.argv[1])
    d = min_distance(xy_list)
    print("distance: %f" % d[0])
    # print_format_solution(d[1])
