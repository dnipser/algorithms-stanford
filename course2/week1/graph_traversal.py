
from course2.week1.graph import Graph, TraversalStatus
from misc.file_utils import read_graph_edges
from os import getenv


def dfs_recursive(vertex, path):
    # return early if the vertex was already traversed
    # than can happen as dfs_traversal is called for all vertices
    # and some of them might be already traversed
    if vertex.status == TraversalStatus.COMPLETED:
        return

    vertex.status = TraversalStatus.IN_PROGRESS
    path.append(vertex)

    for v in vertex.get_neighbors():
        if v.status == TraversalStatus.NOT_VISITED:
            dfs_recursive(v, path)

    vertex.status = TraversalStatus.COMPLETED


def dfs_iterative(vertex, path):
    vertices_to_traverse = [vertex]

    while vertices_to_traverse:
        # remove last element from the stack
        vertex = vertices_to_traverse.pop()

        # skip vertex if it was already traversed
        if vertex.status == TraversalStatus.COMPLETED:
            continue

        vertex.status = TraversalStatus.IN_PROGRESS
        path.append(vertex)

        for v in vertex.get_neighbors():
            if v.status == TraversalStatus.NOT_VISITED:
                vertices_to_traverse.append(v)

        vertex.status = TraversalStatus.COMPLETED


def bfs(vertex, path):
    vertices_to_traverse = [vertex]

    while vertices_to_traverse:
        # remove first element from the stack
        vertex = vertices_to_traverse.pop(0)

        if vertex.status == TraversalStatus.COMPLETED:
            continue

        vertex.status = TraversalStatus.IN_PROGRESS
        path.append(vertex)

        for v in vertex.get_neighbors():
            if v.status == TraversalStatus.NOT_VISITED:
                vertices_to_traverse.append(v)

        vertex.status = TraversalStatus.COMPLETED


def traversal_helper(graph, func):
    # traverse all vertices to handle graphs with multiple roots
    for v in graph.get_vertices():
        path = []
        func(v, path)
        if len(path) > 0:
            print(path)


def main():
    input_graph = read_graph_edges(
        '{}/{}/'.format(getenv('BASE_DIR'), 'course2/week1'),
        'graph.txt')

    traversal_functions = ["dfs_recursive", "dfs_iterative", "bfs"]

    for func in traversal_functions:
        print("traversing graph with: ", func)
        graph = Graph().init(input_graph)
        traversal_helper(graph, globals()[func])
        # print(graph)


if __name__ == '__main__':
    main()
