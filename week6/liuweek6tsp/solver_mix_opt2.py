from solver_opt_2 import *
from solver_or_opt import *
import solver_greedy_liu

def solve():
    path = solver_greedy_liu.solve(cities)[1]
    new_path1 = opt_2(path)
    new_path2 = or_opt(new_path1)
    d = path_distance(new_path2)
    return d, new_path2


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve()
    # print("distance: %f" % solution[0])
    print_format_solution(solution[1])