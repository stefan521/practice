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


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next_node
        return 'SinglyLinkedList(' + ', '.join(values) + ')'

    def __eq__(self, other):
        head_self = self.head
        head_other = other.head

        while head_self is not None and head_other is not None:
            if head_self != head_other:
                return False
            head_self = head_self.next_node
            head_other = head_other.next_node

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def from_list(lst):
        singly_linked_list = SinglyLinkedList()
        for thing in reversed(lst):
            singly_linked_list.prepend(thing)
        return singly_linked_list

    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        new_head = Node(value, self.head)
        self.head = new_head
        return new_head

    # O(n)
    def size(self):
        curr = self.head
        size = 0

        while curr is not None:
            curr = curr.next_node
            size += 1

        return size


# ===== Q1 =====
# O(n)
def remove_duplicates(lst):
    seen = set()

    if lst.is_empty() or lst.head.next_node is None:
        return lst

    current_node = lst.head
    next_node = current_node.next_node
    seen.add(current_node.value)

    while next_node is not None:
        if next_node.value in seen:
            current_node.next_node = next_node.next_node
            next_node = next_node.next_node
        else:
            seen.add(next_node.value)
            current_node = current_node.next_node
            next_node = next_node.next_node

    return lst


# ===== Q3 =====
# O(n)
def to_last(singly_linked_list, kth):
    size = singly_linked_list.size()
    curr = singly_linked_list.head

    if size - kth <= 0:
        return None

    steps = 1
    while steps < size - kth:
        curr = curr.next_node
        steps += 1

    return curr


def to_last_runner_tech(singly_linked_list, kth):
    p1 = singly_linked_list.head
    p2 = singly_linked_list.head
    distance = 0

    while p2 is not None:
        if distance <= kth:
            distance += 1
            p2 = p2.next_node
        else:
            p1 = p1.next_node
            p2 = p2.next_node

    if distance == kth + 1:
        return p1
    else:
        return None


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
