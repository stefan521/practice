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
