"""
Python3
reference: http://www.geocities.jp/m_hiroi/light/pyalgo64.html#list1
"""

import sys
import math
from functions import *


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def create_data(cities):
    """
    Create distance matrix
    """
    tsp_size = len(cities)
    dist = [[0] * tsp_size for i in range(tsp_size)]
    for i in range(tsp_size):
        for j in range(tsp_size):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    return dist


cities = read_input(sys.argv[1])
dist = create_data(cities)
tsp_size = len(cities)


def path_distance(path):
    d = 0
    for i in range(1, len(path)):
        d += dist[path[i-1]][path[i]]
    d += dist[path[-1]][path[0]]
    return d


def opt_2(path):
    while True:
        count = 0
        for i in range(tsp_size - 2):
            i_next = i + 1
            for j in range(i + 2, tsp_size):
                if j == tsp_size - 1:
                    j_next = 0
                else:
                    j_next = j + 1
                if i != 0 or j_next != 0:
                    l1 = dist[path[i]][path[i_next]]
                    l2 = dist[path[j]][path[j_next]]
                    l3 = dist[path[i]][path[j]]
                    l4 = dist[path[i_next]][path[j_next]]
                    if l1 + l2 > l3 + l4:
                        new_path = path[i_next:j + 1]
                        path[i_next:j + 1] = new_path[::-1]
                        count += 1
        if count == 0:
            break
    return path


def solve():
    path = [x for x in range(tsp_size)]
    new_path = opt_2(path)
    d = path_distance(new_path)
    return d, new_path

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve()
    print("distance: %f" % solution[0])
    print_format_solution(solution[1])


