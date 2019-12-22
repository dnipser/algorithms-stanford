
from enum import Enum
from math import inf
from typing import Dict, List, Tuple


class TraversalStatus(Enum):
    NOT_VISITED = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class Vertex:
    def __init__(self, value):
        self.edges = []
        self.value = value
        self.distance = inf
        self.status = TraversalStatus.NOT_VISITED

    def add_edge_to(self, v, weight):
        self.edges.append(Edge(self, v, weight))

    def get_edges(self):
        return self.edges

    def get_value(self):
        return self.value

    def get_distance(self):
        return self.distance

    def __repr__(self):
        return "{}:{}:{}".format(self.value, self.distance, self.status.name)


class Edge:
    def __init__(self, u, v, weight):
        self.vertices = (u, v)
        self.weight = weight

    def get_vertices(self):
        return self.vertices

    def get_tail(self):
        return self.vertices[0]

    def get_head(self):
        return self.vertices[1]

    def get_weight(self):
        return self.weight

    def __repr__(self):
        u_val = self.get_tail().get_value()
        v_val = self.get_head().get_value()
        return "{}>{}".format(str(u_val), str(v_val))


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

    def add_edge(self, u, v, weight) -> None:
        u.add_edge_to(v, weight)

    def get_edges(self):
        edges = []
        for v in self.get_vertices():
            edges.extend(v.get_edges())
        return edges

    def init(self, input: Dict[int, List[Tuple[int, int]]]):
        graph = Graph()

        # initialize graph vertices
        for v in input.keys():
            graph.add_vertex(Vertex(v))

        # read and initialize edges
        for v, n in input.items():
            tail_v = graph.get_vertex_by_value(v)
            connected_vertices = n

            for conn_v, e_weight in connected_vertices:
                head_v = graph.get_vertex_by_value(conn_v)
                graph.add_edge(tail_v, head_v, e_weight)

        return graph

    def __repr__(self):
        res = "Vertices:\n"
        res += ', '.join(str(v) for v in self.get_vertices())
        res += "\n"

        res += "Edges:\n"
        res += ', '.join(str(e) for e in self.get_edges())
        res += "\n"
        return res
