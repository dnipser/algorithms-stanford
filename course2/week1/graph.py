
from enum import Enum
from typing import Dict, List


class TraversalStatus(Enum):
    NOT_VISITED = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class Vertex:
    def __init__(self, value):
        self.out_neighbors = []
        self.value = value
        self.status = TraversalStatus.NOT_VISITED

    def add_neighbor(self, v):
        self.out_neighbors.append(v)

    def remove_neighbor(self, v):
        self.out_neighbors.remove(v)

    def get_neighbors(self):
        return self.out_neighbors

    def get_value(self):
        return self.value

    def __repr__(self):
        return "{}:{}".format(self.value, self.status.name)


class Graph:
    def __init__(self):
        self.vertices = []
        self.value_to_vertex = dict()

    def add_vertex(self, v) -> None:
        self.vertices.append(v)
        self.value_to_vertex[v.value] = v

    def get_vertices(self) -> List[Vertex]:
        return self.vertices

    def get_vertex_by_value(self, v_val):
        res = None
        if v_val in self.value_to_vertex:
            res = self.value_to_vertex[v_val]
        return res

    def add_edge(self, v, u) -> None:
        v.add_neighbor(u)

    def get_edges(self):
        edges = []
        for v in self.get_vertices():
            edges += [(v, u) for u in v.get_neighbors()]
        return edges

    def init(self, input: Dict[int, List[int]]):
        graph = Graph()

        # initialize graph vertices
        for v in input.keys():
            graph.add_vertex(Vertex(v))

        # read and initialize edges
        for v, n in input.items():
            first_vertex = graph.get_vertex_by_value(v)
            connected_v_values = n

            for conn_v_val in connected_v_values:
                second_vertex = graph.get_vertex_by_value(conn_v_val)
                graph.add_edge(first_vertex, second_vertex)

        return graph

    def reset(self):
        for v in self.get_vertices():
            v.status = TraversalStatus.NOT_VISITED

    def __repr__(self):
        res = "Vertices:\n"
        res += ', '.join(str(v) for v in self.get_vertices())
        res += "\n"

        res += "Edges:\n"
        res += ', '.join(str(e) for e in self.get_edges())
        res += "\n"
        return res
