"""
Slove this question follow this:
https://developers.google.com/optimization/routing/tsp/tsp#solving-tsps-with-or-tools
"""
import math
import sys
from functions import *

from google.apputils import app
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def create_data(cities):
    """
    cities 0~4:
    [0.0, 1139.468611035281, 679.7227326641358, 829.251122595876, 740.0208580992705]
    [1139.468611035281, 0.0, 463.63085520669887, 512.7321993957855, 1091.1135139211965]
    [679.7227326641358, 463.63085520669887, 0.0, 394.51229505232465, 745.9866861116151]
    [829.251122595876, 512.7321993957855, 394.51229505232465, 0.0, 1124.5662308439055]
    [740.0208580992705, 1091.1135139211965, 745.9866861116151, 1124.5662308439055, 0.0]
    """
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


def main(_):
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
            print("Total distance: " + str(assignment.ObjectiveValue())+"\n")
            route_number = 0
            index = routing.Start(route_number)
            route = ''
            while not routing.IsEnd(index):
                route += str(city_index[routing.IndexToNode(index)]) + ' -> '
                index = assignment.Value(routing.NextVar(index))
            route += str(city_index[routing.IndexToNode(index)])
            print("Route:\n\n" + route)
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


if __name__ == '__main__':
    app.run()