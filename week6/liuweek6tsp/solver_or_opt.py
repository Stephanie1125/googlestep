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


def or_opt(path):
    while True:
        count = 0
        for i in range(tsp_size):
            i_prev = i - 1
            i_next = i + 1
            if i_prev < 0:
                i_prev = tsp_size - 1
            if i_next == tsp_size:
                i_next = 0
            for j in range(tsp_size):
                j_next = j + 1
                if j_next == tsp_size: j_next = 0
                if j != i and j_next != i:
                    l1 = dist[path[i_prev]][path[i]]
                    l2 = dist[path[i]][path[i_next]]
                    l3 = dist[path[j]][path[j_next]]
                    l4 = dist[path[i_prev]][path[i_next]]
                    l5 = dist[path[j]][path[i]]
                    l6 = dist[path[i]][path[j_next]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        p = path[i]
                        path[i:i + 1] = []
                        if i < j:
                            path[j:j] = [p]
                        else:
                            path[j_next:j_next] = [p]
                        count += 1
        if count == 0:
            break
    return path


def solve():
    path = [x for x in range(tsp_size)]
    new_path = or_opt(path)
    d = path_distance(new_path)
    return d, new_path


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve()
    print("distance: %f" % solution[0])
    print_format_solution(solution[1])

