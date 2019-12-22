
from course2.week2.graph import Graph
from misc.file_utils import read_graph_edges_with_weights
from math import inf
from os import getenv


def get_vertex_with_minimal_distance(vertices):
    res = None
    min_distance = inf
    for v in vertices:
        if v.distance < min_distance:
            min_distance = v.distance
            res = v

    return res


def calculate_shortest_paths(graph):
    # choose first vertex as a starting point
    start_vertex = graph.get_vertices()[0]
    start_vertex.distance = 0

    vertices_to_calculate = []
    vertices_to_calculate.extend(graph.get_vertices())
    while len(vertices_to_calculate) > 0:
        # find vertex with the minimum distance among all remaining vertices
        vertex = get_vertex_with_minimal_distance(vertices_to_calculate)

        # all vertices have been processed or there remain disjoint
        # vertices with infinite distance
        if vertex is None:
            break

        # process edges and update distances
        for edge in vertex.get_edges():
            head_v = edge.get_head()
            if vertex.distance + edge.weight < head_v.distance:
                head_v.distance = vertex.distance + edge.weight

        vertices_to_calculate.remove(vertex)


def explore_graph(graph):
    head_vertices = set()
    for edge in graph.get_edges():
        head_vertices.add(edge.get_head().value)

    for i in range(1, 201):
        head_vertices.remove(i)
    print(head_vertices)


def main():
    input_graph = read_graph_edges_with_weights(
        '{}/{}/'.format(getenv('BASE_DIR'), 'course2/week2'),
        'dijkstraData.txt')

    print("Initializing graph")
    graph = Graph().init(input_graph)
    calculate_shortest_paths(graph)

    vertices_to_check = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    vertex_distances = []
    for v_val in vertices_to_check:
        v_distance = graph.get_vertex_by_value(v_val).distance
        vertex_distances.append(v_distance)

    print(vertex_distances)


if __name__ == '__main__':
    main()
