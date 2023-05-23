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


# ===== Q4 =====
def test_queue_add():
    queue = Queue()

    assert queue.peek() is None

    queue.add(10)
    queue.add(20)
    queue.add(30)

    assert queue.peek() is 10


def test_queue_remove():
    queue = Queue()

    queue.add(10)
    queue.add(20)
    queue.add(30)

    assert queue.remove() is 10
    assert queue.peek() is 20
    assert queue.remove() is 20
    assert queue.peek() is 30
    assert queue.remove() is 30
    assert queue.peek() is None


# ===== Q5 =====
def test_sort_stack_1():
    stack = Stack()
    assert sort_stack(stack).is_empty()


def test_sort_stack_2():
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(10)

    result = sort_stack(stack)

    assert result.pop() is 2
    assert result.pop() is 5
    assert result.pop() is 10


def test_sort_stack_3():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    result = sort_stack(stack)

    assert result.pop() is 1
    assert result.pop() is 2
    assert result.pop() is 3
    assert result.pop() is 4


def test_sort_stack_4():
    stack = Stack()
    stack.push(8)
    stack.push(7)
    stack.push(6)

    result = sort_stack(stack)

    assert result.pop() is 6
    assert result.pop() is 7
    assert result.pop() is 8
