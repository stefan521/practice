class Node:
    def __init__(self, value, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return f"Node({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


class Stack:

    def __init__(self):
        self._top = None

    def pop(self):
        top = self._top

        if top is not None:
            self._top = top.next_node

        return top.value

    def push(self, item):
        old_top = self._top
        self._top = Node(item)
        self._top.next_node = old_top
        return self._top

    def peek(self):
        return self._top

    def is_empty(self):
        return self._top is None


# ===== Q2 =====
def find_min(stack: Stack):
    other_stack = Stack()

    if stack.is_empty():
        return None

    minimum = stack.peek().value

    while not stack.is_empty():
        other_stack.push(stack.pop())
        if other_stack.peek().value < minimum:
            minimum = other_stack.peek().value

    while not other_stack.is_empty():
        stack.push(other_stack.pop())

    return minimum


# ===== Q3 =====
class SetOfStacks:
    def __init__(self, max_stack_size: int = 1):
        self.max_stack_size = max_stack_size
        self.last_stack_size = 0
        self.stack_list: list = []

    def _last_index(self) -> int:
        return len(self.stack_list) - 1

    def push(self, value):
        if len(self.stack_list) == 0 or self.last_stack_size >= self.max_stack_size:
            new_stack = Stack()
            new_stack.push(value)
            self.stack_list.append(new_stack)
            self.last_stack_size = 1
        else:
            self.stack_list[self._last_index()].push(value)
            self.last_stack_size += 1

    def pop(self):
        self.last_stack_size -= 1
        return self.stack_list[self._last_index()].pop()

    def peek(self):
        return self.stack_list[self._last_index()].peek()


# ===== Q4 =====
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        old_tail = self.tail
        self.tail = Node(value)
        if old_tail is not None:
            old_tail.next_node = self.tail
        if self.head is None:
            self.head = self.tail

    def remove(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next_node

        if self.head is None:
            self.tail = None

        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value


# ===== Q5 =====
def sort_stack(stack: Stack) -> Stack:
    sorted_stack = Stack()

    while not stack.is_empty():
        curr = stack.pop()
        if sorted_stack.is_empty() or curr <= sorted_stack.peek().value:
            sorted_stack.push(curr)
        else:
            while not sorted_stack.is_empty() and curr > sorted_stack.peek().value:
                stack.push(sorted_stack.pop())
            sorted_stack.push(curr)

    return sorted_stack

# ===== Q6 =====


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
