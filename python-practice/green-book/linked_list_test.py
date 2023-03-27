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
    expected = 'd'
    result = to_last(lst, 0)
    assert result is not None and result.value == expected


def test_to_last_1():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = 'c'
    result = to_last(lst, 1)
    assert result is not None and result.value == expected


def test_to_last_2():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = 'b'
    result = to_last(lst, 2)
    assert result is not None and result.value == expected


def test_to_last_3():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    expected = 'a'
    result = to_last(lst, 3)
    assert result is not None and result.value == expected


def test_to_last_4():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    result = to_last(lst, 4)
    print(f"result >>>  ${result}")
    assert result is None


def test_to_last_5():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd'])
    result = to_last(lst, 5)
    assert result is None
