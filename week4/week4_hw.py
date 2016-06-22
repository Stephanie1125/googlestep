"""
Implement the pagerank algorithm.
"""


# Create graph structure for the input file
def create_graph(input_file):
    graph = {}
    f = open(input_file, "r")
    for line in f.readlines():
        if line.strip().isdigit():
            continue
        tmp = line.strip().split()
        if len(tmp) == 1:  # node
            graph[tmp[0]] = []
        elif len(tmp) == 2:  # edges
            if tmp[0] in graph:
                graph[tmp[0]] += tmp[1]
        else:
            print "error"
    return graph


# Apply pagerank algorithm
def pagerank(input_file, score):
    model = create_graph(input_file)
    current_score = {}
    previous_score = {}
    # assign initial_score
    for vertex in model:
        previous_score[vertex] = 0
        current_score[vertex] = score
    # if difference is very small, we can say the model is converge and finish the iteration process
    while module_diff(previous_score, current_score) > 0.01:  # iteration process
        previous_score = current_score
        current_score = {x: 0 for x in model}
        for vertex in current_score:
            factor = 1.0 / len(model[vertex])
            for neighbor in model[vertex]:
                current_score[neighbor] += factor * previous_score[vertex]
    return current_score


# for checking difference of the previous score and the current score
def module_diff(previous, current):
    difference = 0
    for i in current:
        difference += (current[i] - previous[i]) ** 2
    return difference ** 0.5


def main():
    print "Results after applied the pagerank algorithm >>"
    print "small data: ", pagerank("sample_inputs/small_data.txt", 100)
    print "medium data: ", pagerank("sample_inputs/medium_data.txt", 100)
    print "large data: ", pagerank("sample_inputs/large_data.txt", 100)


if __name__ == "__main__":
    main()
