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
