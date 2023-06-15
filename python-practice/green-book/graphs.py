class NodeLike:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other: 'NodeLike'):
        return self.value == other.value

    def __ne__(self, other: 'NodeLike'):
        return not self.__eq__(other)

    def __hash__(self):
        return self.value


class Node(NodeLike):
    def __init__(self, value, children=None):
        super().__init__(value)
        self.value = value
        self.children = [] if children is None else children

    def __str__(self):
        return f"Node({self.value})"


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


class BinaryTreeNode(NodeLike):

    def __init__(self, value, left=None, right=None):
        super().__init__(value)
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other: 'BinaryTreeNode'):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __ne__(self, other: 'BinaryTreeNode'):
        return not self.__eq__(other)

    def __str__(self):
        return f"BinaryTreeNode({self.value}, ${self.left}, ${self.right})"


# create a binary search tree from a sorted array of unique numbers
# TODO balance the tree
def array_to_binary_search_tree(numbers: list[int]) -> BinaryTreeNode:
    if len(numbers) == 0:
        return BinaryTreeNode(None)

    root_node = BinaryTreeNode(numbers[0])

    for number in numbers[1:]:
        parent = root_node
        while number < parent.value:
            if parent.left is not None:
                parent = parent.left
            else:
                parent.left = BinaryTreeNode(number)
        while number > parent.value:
            if parent.right is not None:
                parent = parent.right
            else:
                parent.right = BinaryTreeNode(number)

    return root_node


def path_between_nodes_exists(graph: Graph, n1: Node, n2: Node) -> bool:
    for node in graph.nodes:
        connected_subgraph = depth_first_search(node)
        if n1 in connected_subgraph and n2 in connected_subgraph:
            return True

    return False
