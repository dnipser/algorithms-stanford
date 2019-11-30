
from typing import List


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
