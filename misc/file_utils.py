
from typing import Dict, List


def read_input_dataset(dir, file_name):
    input_dataset = []

    path = '{}{}'.format(dir, file_name)
    with open(path) as f:
        for line in f:
            input_dataset.append(int(line))

    return input_dataset


def read_input_graph(dir, file_name) -> List[List[int]]:
    input_graph = []

    path = '{}{}'.format(dir, file_name)
    with open(path) as f:
        for line in f:
            vertices = []
            for num in line.split():
                vertices.append(num)
            input_graph.append(vertices)

    return input_graph


def read_graph_edges(dir, file_name) -> Dict[int, List[int]]:
    input_graph = {}

    path = '{}{}'.format(dir, file_name)
    with open(path) as f:
        for line in f:
            vertices = line.split()
            if len(vertices) != 2:
                print("Invalid input line, ", vertices)
                continue

            out_vertex = vertices[0]
            if out_vertex not in input_graph.keys():
                input_graph[out_vertex] = []

            in_vertex = vertices[1]
            if in_vertex not in input_graph.keys():
                input_graph[in_vertex] = []

            input_graph[out_vertex].append(in_vertex)

    return input_graph
