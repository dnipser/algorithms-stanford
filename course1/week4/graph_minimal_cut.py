

from misc.file_utils import read_input_graph
from itertools import chain
from typing import List
from random import choice
from os import getenv, cpu_count
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, value):
        self.edges = []
        self.value = value

    def add_edge_to(self, v):
        self.edges.append(v)

    def set_edges(self, e):
        self.edges = e

    def get_edges(self):
        return self.edges

    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Edge:
    def __init__(self, v, w):
        self.vertices = (v, w)

    def get_vertices(self):
        return self.vertices

    def get_first_vertex(self):
        return self.vertices[0]

    def get_second_vertex(self):
        return self.vertices[1]

    def __repr__(self):
        v_val = self.get_first_vertex().get_value()
        w_val = self.get_second_vertex().get_value()
        return "{}<>{}".format(str(v_val), str(w_val))


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, v) -> None:
        self.vertices.append(v)

    def get_vertices(self) -> List[Vertex]:
        return self.vertices

    def get_vertex_by_value(self, v_val):
        res = None
        for v in self.vertices:
            if v.get_value() == v_val:
                res = v
                break
        return res

    def get_edges(self) -> List[Edge]:
        edges = [Edge(v, ev) for v in self.vertices for ev in v.get_edges()]
        return edges

    def merge(self, v, w) -> None:
        merged_val = "{}:{}".format(v.get_value(), w.get_value())
        merged_vertex = Vertex(merged_val)

        merged_vertices = []
        for ev in chain(v.get_edges(), w.get_edges()):
            # skip vertices being merged to eliminate self references
            if not (ev == v or ev == w):
                merged_vertices.append(ev)
        merged_vertex.set_edges(merged_vertices)

        # update back references to point to merged vertex
        for mv in merged_vertices:
            if v in mv.get_edges():
                mv.get_edges().remove(v)
                mv.add_edge_to(merged_vertex)

            if w in mv.get_edges():
                mv.get_edges().remove(w)
                mv.add_edge_to(merged_vertex)

        self.vertices.append(merged_vertex)
        self.vertices.remove(v)
        self.vertices.remove(w)

    def calculate_min_cut(self) -> int:
        while len(self.get_vertices()) > 2:
            edge = choice(self.get_edges())
            self.merge(edge.get_first_vertex(), edge.get_second_vertex())

        first_vertex = self.get_vertices()[0]
        return len(first_vertex.get_edges())

    def __str__(self):
        res = "Vertices:\n"
        res += ', '.join(str(v) for v in self.get_vertices())
        res += "\n"

        res += "Edges:\n"
        res += ', '.join(str(e) for e in self.get_edges())
        res += "\n"
        return res


def init_graph(input: List[List[int]]) -> Graph:
    graph = Graph()

    # initialize graph vertices
    for line in input:
        graph.add_vertex(Vertex(line[0]))

    # read and initialize edges
    for line in input:
        first_vertex = graph.get_vertex_by_value(line[0])
        connected_v_values = line[1:]

        for conn_v_val in connected_v_values:
            second_vertex = graph.get_vertex_by_value(conn_v_val)
            first_vertex.add_edge_to(second_vertex)

    return graph


def calculate_task(input_graph):
    graph = init_graph(input_graph)
    result = graph.calculate_min_cut()
    print("Received result of graph min cut: {}".format(result))
    return result


def main():
    input_graph = read_input_graph(
        '{}/{}/'.format(getenv('BASE_DIR'), 'course1/week4'),
        'kargerMinCut.txt')

    num_of_cores = cpu_count()
    if num_of_cores is None:
        num_of_cores = 3

    futures = []
    attempt = 1
    attempts = 1000
    with ThreadPoolExecutor(max_workers=num_of_cores) as executor:
        for n in range(attempts):
            futures.append(executor.submit(calculate_task, input_graph))
            print("Submitted calculation task {}".format(attempt))
            attempt += 1

    cuts = []
    for future in as_completed(futures):
        cut_value = future.result()
        cuts.append(cut_value)

    plt.hist(cuts, 100, facecolor='green')
    plt.savefig('{}/{}/{}'.format(getenv('BASE_DIR'), 'course1/week4', 'cut_distribution.png'))

    print(cuts)
    print(min(cuts))


if __name__ == '__main__':
    main()
