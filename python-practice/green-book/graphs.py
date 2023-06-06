class NodeId:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"NodeId({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


class Node:
    def __init__(self, node_id: NodeId):
        self.node_id = node_id

    def __str__(self):
        return f"Node({self.node_id})"

    def __eq__(self, other):
        return self.node_id == other.node_id

    def __ne__(self, other):
        return not self.__eq__(other)


class UndirectedGraph:
    def __init__(self, nodes: list[Node], edges: set[tuple[NodeId, NodeId]]):
        self.nodes = nodes
        self.edges = edges


class DirectedGraph:
    def __init__(self, nodes: list[Node], edges: dict[NodeId, NodeId]):
        self.nodes = nodes
        self.edges = edges


class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = [] if children is None else children

    def __str__(self):
        return f"TreeNode({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


def breadth_first_search(tree: TreeNode) -> list[TreeNode]:
    visited = []
    to_visit = [tree]

    while to_visit:
        node = to_visit.pop(0)
        visited.append(node)
        for descendant in node.children:
            to_visit.append(descendant)

    return visited


def depth_first_search(tree: TreeNode) -> list[TreeNode]:
    visited = []

    for descendant in tree.children:
        visited.extend(depth_first_search(descendant))
    visited.append(tree)

    return visited
