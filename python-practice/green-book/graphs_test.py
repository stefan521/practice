from graphs import *


def test_breadth_first_search_0():
    tree = TreeNode(0)
    result = breadth_first_search(tree)
    assert result == [tree]


def test_breadth_first_search_1():
    tree = TreeNode(
        0,
        [
            TreeNode(1,
                     [
                         TreeNode(3)
                     ]
                     ),
            TreeNode(2)
        ]
    )

    result = breadth_first_search(tree)
    assert result == [TreeNode(0), TreeNode(1), TreeNode(2), TreeNode(3)]


def test_depth_first_search_0():
    tree = TreeNode(0)
    result = depth_first_search(tree)
    assert result == [tree]


def test_depth_first_search_1():
    tree = TreeNode(
        0,
        [
            TreeNode(1,
                     [
                         TreeNode(3)
                     ]
                     ),
            TreeNode(2)
        ]
    )

    result = depth_first_search(tree)
    assert result == [TreeNode(3), TreeNode(1), TreeNode(2), TreeNode(0)]
