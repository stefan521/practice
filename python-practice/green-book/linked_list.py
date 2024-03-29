class Node:
    def __init__(self, value, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return f"Node({self.value})"

    def __eq__(self, other: 'Node'):
        return self.value == other.value

    def __ne__(self, other: 'Node'):
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

    def __eq__(self, other: 'SinglyLinkedList'):
        head_self = self.head
        head_other = other.head

        while head_self is not None and head_other is not None:
            if head_self != head_other:
                return False
            head_self = head_self.next_node
            head_other = head_other.next_node

        return True

    def __ne__(self, other: 'SinglyLinkedList'):
        return not self.__eq__(other)

    @staticmethod
    def from_list(lst: list):
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
def remove_duplicates(lst: SinglyLinkedList):
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


# ===== Q2 =====
# O(n)
def to_last(singly_linked_list: SinglyLinkedList, kth: int):
    size = singly_linked_list.size()
    curr = singly_linked_list.head

    if size - kth <= 0:
        return None

    steps = 1
    while steps < size - kth:
        curr = curr.next_node
        steps += 1

    return curr


def to_last_runner_tech(singly_linked_list: SinglyLinkedList, kth: int):
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


# ===== Q3 =====
def delete_middle_node(singly_linked_list: SinglyLinkedList):
    p1 = singly_linked_list.head
    p2 = singly_linked_list.head

    if p1 is None or p1.next_node is None:
        singly_linked_list.head = None
        return singly_linked_list

    while p2 is not None and p2.next_node is not None:
        if p1 is not p2:
            p1 = p1.next_node
        p2 = p2.next_node.next_node

    if p2 is not None:
        p1.next_node = p1.next_node.next_node

    return singly_linked_list


# ===== Q4 =====
def partition(lst: SinglyLinkedList, partition_value: int):
    new_lst = SinglyLinkedList.from_list([])

    if lst.head is None:
        return new_lst

    new_lst.prepend(lst.head.value)
    new_lst_tail = new_lst.head
    curr = lst.head.next_node

    while curr is not None:
        if curr.value < partition_value:
            new_lst.prepend(curr.value)

        if curr.value >= partition_value:
            new_lst_tail.next_node = Node(curr.value)
            new_lst_tail = new_lst_tail.next_node

        curr = curr.next_node

    return new_lst


# ===== Q5 =====
def _sum_lst_reversed(lst: SinglyLinkedList):
    total = 0
    multiplier = 0
    curr = lst.head

    while curr is not None:
        total += curr.value * pow(10, multiplier)
        multiplier += 1
        curr = curr.next_node

    return total


def sum_numbers_reversed(n1: SinglyLinkedList, n2: SinglyLinkedList):
    return _sum_lst_reversed(n1) + _sum_lst_reversed(n2)


# ===== Q6 =====
def is_palindrome(lst: SinglyLinkedList):
    new_lst = SinglyLinkedList.from_list([])
    curr = lst.head

    while curr is not None:
        new_lst.prepend(curr.value)
        curr = curr.next_node

    return lst == new_lst


# ===== Q7 =====
def find_intersection(lst1: SinglyLinkedList, lst2: SinglyLinkedList):
    lst1_nodes = set()

    curr = lst1.head
    while curr is not None:
        lst1_nodes.add(id(curr))
        curr = curr.next_node

    curr = lst2.head
    while curr is not None:
        if id(curr) in lst1_nodes:
            return curr
        curr = curr.next_node

    return None


# ===== Q8 =====
def find_cycle(lst: SinglyLinkedList):
    lst_nodes = set()

    curr = lst.head
    while curr is not None:
        if id(curr) in lst_nodes:
            return curr
        else:
            lst_nodes.add(id(curr))
        curr = curr.next_node

    return None


def main():
    print("run python3 -m pytest")


if __name__ == "__main__":
    main()
