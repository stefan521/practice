from stacks_and_queues import *


def test_is_empty():
    empty_stack = Stack()
    assert empty_stack.is_empty()


def test_is_not_empty():
    stack = Stack()
    stack.push(3)
    assert not stack.is_empty()


def test_peek_empty():
    empty_stack = Stack()
    assert empty_stack.peek() is None


def test_peek_non_empty():
    stack = Stack()
    stack.push(3)
    stack.push(5)
    assert stack.peek().value == 5


def test_push():
    stack = Stack()
    stack.push(2)
    stack.push(9)
    stack.push(10)
    assert stack._top.value == 10


def test_pop():
    stack = Stack()
    stack.push(2)
    stack.push(9)
    stack.push(10)
    assert stack.pop() is 10
    assert stack._top.value == 9


# ===== Q2 =====
def test_find_min_0():
    stack = Stack()
    assert find_min(stack) is None


def test_find_min_1():
    stack = Stack()
    stack.push(22)
    stack.push(521)
    stack.push(13)
    stack.push(90)
    assert find_min(stack) is 13


def test_find_min_2():
    stack = Stack()
    stack.push(20)
    assert find_min(stack) is 20
