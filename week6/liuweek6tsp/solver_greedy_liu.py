#!/usr/bin/env python3

import sys
import math
from functions import *


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    # track_min = {}
    # find_min_d = []
    distance_result = 0
    d = 0

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    #         track_min[distance(cities[i], cities[j])] = [i, j]
    #         if i != j:
    #             find_min_d.append(distance(cities[i], cities[j]))
    # print find_min_d
    # min_d = min(find_min_d)  # key
    # print min_d
    # print "start index: %d" % track_min[min_d][0]
    # current_city = track_min[min_d][0]

    track_d = []

    for i in range(N):
        current_city = i

        unvisited_cities = set(range(N))
        unvisited_cities.remove(current_city)
        # print unvisited_cities
        solution = [current_city]

        def distance_from_current_city(to):
            return dist[current_city][to]

        while unvisited_cities:
            next_city = min(unvisited_cities, key=distance_from_current_city)
            distance_result += distance(cities[current_city],cities[next_city])
            unvisited_cities.remove(next_city)
            solution.append(next_city)
            current_city = next_city
        distance_result += distance(cities[solution[-1]], cities[solution[0]])
        for i in range(1, len(solution)):
            d += distance(cities[solution[i-1]], cities[solution[i]])
        d += distance(cities[solution[-1]],cities[solution[0]])
        track_d.append(d)
        d = 0
    # return solution, distance_result, d
    return track_d


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_format_solution(solution)
