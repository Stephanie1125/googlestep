"""
Python3
"""


def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def print_format_solution(solution):
    print ('index\n' + '\n'.join(map(str, solution)))



