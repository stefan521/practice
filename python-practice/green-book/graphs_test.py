from graphs import *


def test_breadth_first_search_0():
    tree = Node(0)
    result = breadth_first_search(tree)
    assert result == [tree]


def test_breadth_first_search_1():
    tree = Node(
        0,
        [
            Node(1,
                 [
                         Node(3)
                     ]
                 ),
            Node(2)
        ]
    )

    result = breadth_first_search(tree)
    assert result == [Node(0), Node(1), Node(2), Node(3)]


def test_depth_first_search_0():
    tree = Node(0)
    result = depth_first_search(tree)
    assert result == [tree]


def test_depth_first_search_1():
    tree = Node(
        0,
        [
            Node(1,
                 [
                         Node(3)
                     ]
                 ),
            Node(2)
        ]
    )

    result = depth_first_search(tree)
    assert result == [Node(3), Node(1), Node(2), Node(0)]


def test_path_between_nodes_exists_0():
    graph = Graph([])

    result = path_between_nodes_exists(graph, Node(1), Node(2))

    assert result is False


def test_path_between_nodes_exists_1():
    n3 = Node(3)
    n2 = Node(2, [n3])
    n1 = Node(1, [n2])
    graph = Graph([n1, n2, n3])

    result = path_between_nodes_exists(graph, n1, n3)

    assert result is True


def test_path_between_nodes_exists_2():
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3, [n4, n5])
    n2 = Node(2)
    n1 = Node(1, [n2])
    graph = Graph([n1, n2, n3])

    result = path_between_nodes_exists(graph, n1, n3)

    assert result is False
