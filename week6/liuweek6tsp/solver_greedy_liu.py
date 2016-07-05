#!/usr/bin/env python3

import sys
import math
from functions import *


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    track_min = {}
    find_min_d = []

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            track_min[distance(cities[i], cities[j])] = [i, j]
            if i != j:
                find_min_d.append(distance(cities[i], cities[j]))
    min_d = min(find_min_d)  # key
    current_city = track_min[min_d][0]

    for i in range(N):
        distance_result = 0
        current_city = i
        unvisited_cities = set(range(N))
        unvisited_cities.remove(current_city)
        path = [current_city]

        def distance_from_current_city(to):
            return dist[current_city][to]

        while unvisited_cities:
            next_city = min(unvisited_cities, key=distance_from_current_city)
            distance_result += distance(cities[current_city],cities[next_city])
            unvisited_cities.remove(next_city)
            path.append(next_city)
            current_city = next_city
        distance_result += distance(cities[path[-1]], cities[path[0]])
    return distance_result, path


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print("distance: %f" % solution[0])
    print_format_solution(solution[1])
