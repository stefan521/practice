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


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
