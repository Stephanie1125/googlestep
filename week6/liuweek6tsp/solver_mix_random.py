"""
for input_6.csv - random
"""
from solver_opt_2 import *
from solver_or_opt import *
import random

current_score = 42378.641570


def format_solution(solution):
    return 'index\n' + '\n'.join(map(str, solution))


def solve():
    path = [x for x in range(tsp_size)]
    random.shuffle(path)
    new_path1 = opt_2(path)
    new_path2 = or_opt(new_path1)
    d = path_distance(new_path2)
    return d, new_path2


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve()
    print("distance: %f" % solution[0])
    if solution[0] < current_score:   # overwrite the solution if obtain better score
        with open('solution_google_opt_6.csv', 'w') as f:
            f.write(format_solution(solution[1]) + '\n')