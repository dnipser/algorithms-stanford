
from typing import Dict, List, Tuple


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

            tail_v = int(vertices[0])
            if tail_v not in input_graph.keys():
                input_graph[tail_v] = []

            head_v = int(vertices[1])
            if head_v not in input_graph.keys():
                input_graph[head_v] = []

            input_graph[tail_v].append(head_v)

    return input_graph


def read_graph_edges_with_weights(dir, file_name) -> Dict[int, List[Tuple[int, int]]]:
    input_graph = {}

    path = '{}{}'.format(dir, file_name)
    with open(path) as f:
        for line in f:
            vertices = line.split()

            tail_v = int(vertices[0])
            if tail_v not in input_graph.keys():
                input_graph[tail_v] = []

            head_vertices = vertices[1:]
            for vertex_line in head_vertices:
                h_v_weight = vertex_line.split(',')
                input_graph[tail_v].append(
                    (int(h_v_weight[0]), int(h_v_weight[1])))

    return input_graph
