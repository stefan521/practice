from linked_list import *


# ===== Q1 =====
def test_remove_duplicates_0():
    lst = SinglyLinkedList()
    expected = SinglyLinkedList()
    assert remove_duplicates(lst) == expected


def test_remove_duplicates_1():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'c', 'b', 'd', 'a', 'v'])
    expected = SinglyLinkedList.from_list(['a', 'b', 'c', 'd', 'v'])
    assert remove_duplicates(lst) == expected


# ===== Q2 =====
def test_to_last_0():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = Node('d')
    assert to_last(lst, 0) == expected
    assert to_last_runner_tech(lst, 0) == expected


def test_to_last_1():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = Node('c')
    assert to_last(lst, 1) == expected
    assert to_last_runner_tech(lst, 1) == expected


def test_to_last_2():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = Node('b')
    assert to_last(lst, 2) == expected
    assert to_last_runner_tech(lst, 2) == expected


def test_to_last_3():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = Node('a')
    assert to_last(lst, 3) == expected
    assert to_last_runner_tech(lst, 3) == expected


def test_to_last_4():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    assert to_last(lst, 4) is None
    assert to_last_runner_tech(lst, 4) is None


def test_to_last_5():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    assert to_last(lst, 5) is None
    assert to_last_runner_tech(lst, 5) is None


# ===== Q3 =====
def test_delete_midddle_node_0():
    lst = SinglyLinkedList.from_list([])
    expected = SinglyLinkedList.from_list([])
    assert delete_midddle_node(lst) == expected


def test_delete_midddle_node_1():
    lst = SinglyLinkedList.from_list(['a'])
    expected = SinglyLinkedList.from_list([])
    assert delete_midddle_node(lst) == expected


def test_delete_midddle_node_2():
    lst = SinglyLinkedList.from_list(['a', 'b'])
    expected = SinglyLinkedList.from_list(['a', 'b'])
    assert delete_midddle_node(lst) == expected


def test_delete_midddle_node_3():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c'])
    expected = SinglyLinkedList.from_list(['a', 'c'])
    assert delete_midddle_node(lst) == expected


# ===== MISC =====
def test_node_equality():
    n1 = Node('a')
    n2 = Node('a')
    n3 = Node('b')
    assert n1 == n2
    assert n1 != n3
    assert n1 is not n2
    assert n1 is not n3
