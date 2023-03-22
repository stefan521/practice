from linked_list import *


# ===== Q1 =====
def test_remove_duplicates_0():
    lst = []
    expected = []
    assert remove_duplicates(lst) == expected


def test_remove_duplicates_1():
    lst = ['a', 'b', 'c', 'c', 'd', 'a', 'v']
    expected = ['a', 'b', 'c', 'd', 'v']
    assert remove_duplicates(lst) == expected
