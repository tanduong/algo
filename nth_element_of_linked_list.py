class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value)

def nth_from_last(head, n):
    current = head
    length = 0
    while current:
        current = current.child
        length += 1

    if length < n:
        return None

    current = head
    for i in range(length - n):
        current = current.child

    return current.value

def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.child
    str_list.append('(None)')
    return ' -> '.join(str_list)

current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2

import unittest

class TestHead(unittest.TestCase):
    def test_one(self):
        # import pdb; pdb.set_trace()
        self.assertEqual(nth_from_last(head, 1), 1)
        self.assertEqual(nth_from_last(head, 5), 5)
        self.assertEqual(nth_from_last(head2, 2), 3)
        self.assertEqual(nth_from_last(head2, 4), 1)
        self.assertEqual(nth_from_last(head2, 5), None)
        self.assertEqual(nth_from_last(None, 1), None)
