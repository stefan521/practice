from cci_book.linked_list import *


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
def test_delete_middle_node_0():
    lst = SinglyLinkedList.from_list([])
    expected = SinglyLinkedList.from_list([])
    assert delete_middle_node(lst) == expected


def test_delete_middle_node_1():
    lst = SinglyLinkedList.from_list(['a'])
    expected = SinglyLinkedList.from_list([])
    assert delete_middle_node(lst) == expected


def test_delete_middle_node_2():
    lst = SinglyLinkedList.from_list(['a', 'b'])
    expected = SinglyLinkedList.from_list(['a', 'b'])
    assert delete_middle_node(lst) == expected


def test_delete_middle_node_3():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c'])
    expected = SinglyLinkedList.from_list(['a', 'c'])
    assert delete_middle_node(lst) == expected


# ===== Q4 =====
def test_partition_lst_0():
    lst = SinglyLinkedList.from_list([])
    expected = SinglyLinkedList.from_list([])
    assert partition(lst, 0) == expected


def test_partition_lst_1():
    lst = SinglyLinkedList.from_list([4])
    expected = SinglyLinkedList.from_list([4])
    assert partition(lst, 0) == expected


def test_partition_lst_2():
    lst = SinglyLinkedList.from_list([5, 10])
    expected = SinglyLinkedList.from_list([5, 10])
    assert partition(lst, 0) == expected


def test_partition_lst_3():
    lst = SinglyLinkedList.from_list([8, 9, 1])
    expected = SinglyLinkedList.from_list([1, 8, 9])
    assert partition(lst, 5) == expected


def test_partition_lst_4():
    lst = SinglyLinkedList.from_list([3, 5, 8, 5, 10, 2, 1])
    expected = SinglyLinkedList.from_list([1, 2, 3, 5, 8, 5, 10])
    assert partition(lst, 5) == expected


# ===== Q5 =====
def test_sum_numbers_reversed_0():
    lst1 = SinglyLinkedList.from_list([])
    lst2 = SinglyLinkedList.from_list([])
    assert sum_numbers_reversed(lst1, lst2) == 0


def test_sum_numbers_reversed_1():
    lst1 = SinglyLinkedList.from_list([])
    lst2 = SinglyLinkedList.from_list([5, 1, 2])
    assert sum_numbers_reversed(lst1, lst2) == 215


def test_sum_numbers_reversed_2():
    lst1 = SinglyLinkedList.from_list([3, 6, 8])
    lst2 = SinglyLinkedList.from_list([])
    assert sum_numbers_reversed(lst1, lst2) == 863


def test_sum_numbers_reversed_3():
    lst1 = SinglyLinkedList.from_list([7, 1, 6])
    lst2 = SinglyLinkedList.from_list([5, 9, 2])
    assert sum_numbers_reversed(lst1, lst2) == 912


def test_sum_numbers_reversed_4():
    lst1 = SinglyLinkedList.from_list([0, 1])
    lst2 = SinglyLinkedList.from_list([2])
    assert sum_numbers_reversed(lst1, lst2) == 12


# ===== Q6 =====
def test_palindrome_0():
    assert is_palindrome(SinglyLinkedList.from_list([]))
    assert is_palindrome(SinglyLinkedList.from_list([4]))
    assert is_palindrome(SinglyLinkedList.from_list([5, 5]))
    assert is_palindrome(SinglyLinkedList.from_list([5, 2, 5]))
    assert not is_palindrome(SinglyLinkedList.from_list([5, 3]))
    assert not is_palindrome(SinglyLinkedList.from_list([2, 2, 5]))
    assert is_palindrome(SinglyLinkedList.from_list(['a', 'b', 'b', 'a']))
    assert is_palindrome(SinglyLinkedList.from_list(['a', 'c', 'v', 'c', 'a']))
    assert not is_palindrome(SinglyLinkedList.from_list(['a', 'x', 'b', 'a']))
    assert not is_palindrome(SinglyLinkedList.from_list(['a', 'x', 'v', 'c', 'a']))


# ===== Q7 =====
def test_find_intersection_0():
    lst1 = SinglyLinkedList.from_list([])
    lst2 = SinglyLinkedList.from_list([])
    assert find_intersection(lst1, lst2) is None


def test_find_intersection_1():
    lst1 = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    lst2 = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    assert find_intersection(lst1, lst2) is None


def test_find_intersection_2():
    lst1 = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    lst2 = SinglyLinkedList.from_list([])
    lst2.head = lst1.head.next_node.next_node

    assert find_intersection(lst1, lst2) is lst2.head


# ===== Q8 =====
def test_find_cycle_0():
    lst = SinglyLinkedList.from_list([])
    assert find_cycle(lst) is None


def test_find_cycle_1():
    lst = SinglyLinkedList.from_list(['a', 'b', 'c', 'd', 'e', 'f'])
    assert find_cycle(lst) is None


def test_find_cycle_2():
    lst = SinglyLinkedList.from_list([])
    c = Node('c')
    b = Node('b', c)
    a = Node('a', b)
    c.next_node = b
    lst.head = a
    assert find_cycle(lst) is b


# ===== MISC =====
def test_node_equality():
    n1 = Node('a')
    n2 = Node('a')
    n3 = Node('b')
    assert n1 == n2
    assert n1 != n3
    assert n1 is not n2
    assert n1 is not n3
