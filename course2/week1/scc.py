
from datetime import datetime
from misc.file_utils import read_graph_edges
from course2.week1.graph import Graph, TraversalStatus
from os import getenv


def dfs_iterative(vertex, stack):
    vertices_to_traverse = [vertex]
    vertex.status = TraversalStatus.COMPLETED

    while vertices_to_traverse:
        # peek last element from the stack
        vertex = vertices_to_traverse[-1]

        for v in vertex.get_neighbors():
            if v.status == TraversalStatus.NOT_VISITED:
                v.status = TraversalStatus.COMPLETED
                vertices_to_traverse.append(v)

        if vertex == vertices_to_traverse[-1]:
            removed = vertices_to_traverse.pop()
            stack.append(removed.value)


def explore_edges(graph):
    empty_neighbors = 0
    for vertex in graph.get_vertices():
        if len(vertex.get_neighbors()) == 0:
            empty_neighbors += 1

        for next_neighbor in vertex.get_neighbors():
            if next_neighbor is None:
                print("Found empty neighbor for vertex ", vertex)

    print("Found vertices with empty neighbors ", empty_neighbors)


def explore_traversed(graph):
    non_visited = 0
    for vertex in graph.get_vertices():
        if vertex.status == TraversalStatus.NOT_VISITED:
            non_visited += 1

    print("Found non visited vertices ", non_visited)


def print_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


def scc_kosaraju(graph, reverse_graph):
    """
    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9A%D0%BE%D1%81%D0%B0%D1%80%D0%B0%D0%B9%D1%8E
    https://www.youtube.com/watch?v=5wFyZJ8yH9Q&t=1s
    """
    scc_paths = []
    traversed_path = []

    for vertex in reverse_graph.get_vertices():
        if vertex.status == TraversalStatus.NOT_VISITED:
            dfs_iterative(vertex, traversed_path)

    while traversed_path:
        vertex_val = traversed_path.pop()
        vertex = graph.get_vertex_by_value(vertex_val)

        if vertex.status == TraversalStatus.NOT_VISITED:
            traversed_vertices = []
            dfs_iterative(vertex, traversed_vertices)
            scc_paths.append(traversed_vertices)

    ssc_lengts = []
    for path in scc_paths:
        ssc_lengts.append(len(path))

    top_scc = sorted(ssc_lengts, reverse=True)[:5]
    print("SCC complete, top 5 components, ", top_scc)
    print("Total SCCs ", len(scc_paths))


def main():
    input_graph = read_graph_edges(
        '{}/{}/'.format(getenv('BASE_DIR'), 'course2/week1'),
        'SCC_Edges.txt')

    print("Initializing graph")
    print_current_time()
    graph = Graph().init(input_graph)
    reversed_graph = graph.reverse()
    print_current_time()

    print("Starting graph analysis")
    print_current_time()
    scc_kosaraju(graph, reversed_graph)
    print_current_time()


if __name__ == '__main__':
    main()
