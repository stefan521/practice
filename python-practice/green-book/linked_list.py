# ===== Q1 =====

class Node:
    def __init__(self, next_node, value):
        self.next_node = next_node
        self.value = value


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next_node
        return '[' + ', '.join(reversed(values)) + ']'

    @staticmethod
    def from_list(lst):
        singly_linked_list = SinglyLinkedList()
        for thing in lst:
            singly_linked_list.append(thing)
        return singly_linked_list

    def is_empty(self):
        return self.head is None

    def append(self, value):
        new_head = Node(self.head, value)
        self.head = new_head
        return new_head


def remove_duplicates(lst):
    seen = set()
    new_list = []

    for element in lst:
        if element not in seen:
            new_list.append(element)
            seen.add(element)

    return new_list


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
