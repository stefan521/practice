class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = [] if children is None else children

    def __str__(self):
        return f"Node({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.value


class Graph:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes


def breadth_first_search(tree: Node) -> list[Node]:
    visited = []
    to_visit = [tree]

    while to_visit:
        node = to_visit.pop(0)
        visited.append(node)
        for descendant in node.children:
            to_visit.append(descendant)

    return visited


def depth_first_search(tree: Node) -> list[Node]:
    visited = []

    for descendant in tree.children:
        visited.extend(depth_first_search(descendant))
    visited.append(tree)

    return visited


def path_between_nodes_exists(graph: Graph, n1: Node, n2: Node) -> bool:
    for node in graph.nodes:
        connected_subgraph = depth_first_search(node)
        if n1 in connected_subgraph and n2 in connected_subgraph:
            return True

    return False
