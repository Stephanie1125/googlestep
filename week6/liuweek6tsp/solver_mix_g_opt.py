"""
Solve this question follow this:
https://developers.google.com/optimization/routing/tsp/tsp#solving-tsps-with-or-tools
"""
from google.apputils import app
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

from solver_opt_2 import *
from solver_or_opt import *


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def create_data(cities):
    tsp_size = len(cities)
    dist = [[0] * tsp_size for i in range(tsp_size)]
    for i in range(tsp_size):
        for j in range(tsp_size):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    return dist


class CreateDistanceCallback(object):
    def __init__(self, cities):
        self.matrix = create_data(cities)

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]


def main(_):  # '_' is a valid variable name(I think it is used in the library)
    path = get_path(_)
    new_path1 = opt_2(path)
    new_path2 = or_opt(new_path1)
    d = path_distance(new_path2)
    print('index')
    for i in new_path2:
        print(i)


def get_path(_):
    cities = read_input(sys.argv[1])
    city_index = [x for x in range(len(cities))]
    tsp_size = len(cities)
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, 1)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        dist_between_nodes = CreateDistanceCallback(cities)
        dist_callback = dist_between_nodes.Distance
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            route_number = 0
            index = routing.Start(route_number)
            route = ''
            while not routing.IsEnd(index):
                route += str(city_index[routing.IndexToNode(index)]) + '\n'
                index = assignment.Value(routing.NextVar(index))
            route += str(city_index[routing.IndexToNode(index)])
            path = map(int, route.split('\n'))
            return path
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


if __name__ == '__main__':
    app.run()